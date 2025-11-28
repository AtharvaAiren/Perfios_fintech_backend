from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models
from app.deps import get_db, get_current_user

router = APIRouter()

@router.post("/create")
def create_consent(
    c: schemas.ConsentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    farmer = db.query(models.Farmer).filter(models.Farmer.id == c.farmer_id).first()
    if not farmer or farmer.user_id != user.id:
        return {"error": "farmer not found or unauthorized"}

    consent = models.Consent(
        farmer_id=c.farmer_id,
        purpose=c.purpose,
        scope=c.scope
    )
    db.add(consent)
    db.commit()
    db.refresh(consent)

    return {"id": consent.id, "granted": consent.granted}
