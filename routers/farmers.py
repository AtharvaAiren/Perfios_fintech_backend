from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models
from app.deps import get_db, get_current_user

router = APIRouter()

@router.post("/create")
def create_farmer(
    farmer_in: schemas.FarmerCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    farmer = models.Farmer(
        user_id=user.id,
        name=farmer_in.name,
        aadhaar=farmer_in.aadhaar,
        pan=farmer_in.pan
    )
    db.add(farmer)
    db.commit()
    db.refresh(farmer)
    return {"id": farmer.id, "name": farmer.name}
