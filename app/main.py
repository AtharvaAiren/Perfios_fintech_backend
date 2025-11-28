from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, farmers, consents, applications, bankstatements
from app import models

app = FastAPI(title="AgriSure Backend")

# Local development only (in production use Alembic!)
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(farmers.router, prefix="/farmers", tags=["farmers"])
app.include_router(consents.router, prefix="/consents", tags=["consents"])
app.include_router(applications.router, prefix="/applications", tags=["applications"])
app.include_router(bankstatements.router, prefix="/bank", tags=["bank"])
