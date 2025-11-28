from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db, get_current_user
from app import models
from app.storage import upload_file
from app.tasks import process_bank_statement

router = APIRouter()

@router.post("/upload")
def upload(
    file: UploadFile = File(...),
    farmer_id: int = None,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    farmer = db.query(models.Farmer).filter(models.Farmer.id == farmer_id).first()
    if not farmer or farmer.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    contents = file.file.read()
    local_path = f"/tmp/{file.filename}"

    with open(local_path, "wb") as f:
        f.write(contents)

    stored = upload_file(local_path, f"bank_statements/{file.filename}")

    bs = models.BankStatement(
        farmer_id=farmer_id,
        file_path=stored
    )
    db.add(bs)
    db.commit()
    db.refresh(bs)

    return {"id": bs.id, "file_path": bs.file_path}

@router.post("/process")
def process(bank_statement_id: int, application_id: int = None):
    task = process_bank_statement.delay(bank_statement_id, application_id)
    return {"task_id": task.id, "status": "queued"}
