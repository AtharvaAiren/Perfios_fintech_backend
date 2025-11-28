from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models
from app.deps import get_db, get_current_user
from app.tasks import process_bank_statement

router = APIRouter()

@router.post("/create", response_model=schemas.ApplicationOut)
def create_application(
    a: schemas.ApplicationCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    farmer = db.query(models.Farmer).filter(models.Farmer.id == a.farmer_id).first()
    if not farmer or farmer.user_id != user.id:
        return {"error": "farmer not found or unauthorized"}

    app_obj = models.Application(
        farmer_id=a.farmer_id,
        product=a.product,
        status="pending"
    )
    db.add(app_obj)
    db.commit()
    db.refresh(app_obj)

    return app_obj

@router.get("/status/{id}", response_model=schemas.ApplicationOut)
def status(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    app_obj = db.query(models.Application).filter(models.Application.id == id).first()
    if not app_obj:
        return {"error": "application not found"}

    return app_obj
