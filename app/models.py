from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Farmer(Base):
    __tablename__ = "farmers"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    aadhaar = Column(String, unique=True, index=True, nullable=True)
    pan = Column(String, unique=True, index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

class Consent(Base):
    __tablename__ = "consents"
    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"), nullable=False)
    purpose = Column(String, nullable=False)
    scope = Column(JSON, nullable=True)
    granted = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    farmer = relationship("Farmer")

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"), nullable=False)
    product = Column(String, nullable=False)
    status = Column(String, default="pending")
    result = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    farmer = relationship("Farmer")

class BankStatement(Base):
    __tablename__ = "bank_statements"
    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"), nullable=False)
    file_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    perfios_result_id = Column(Integer, ForeignKey("perfios_results.id"), nullable=True)

    farmer = relationship("Farmer")
    perfios_result = relationship("PerfiosResult", back_populates="bank_statement")

class PerfiosResult(Base):
    __tablename__ = "perfios_results"
    id = Column(Integer, primary_key=True, index=True)
    raw = Column(JSON, nullable=False)
    summary = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    bank_statement = relationship("BankStatement", uselist=False, back_populates="perfios_result")

class OneVigilResult(Base):
    __tablename__ = "onevigil_results"
    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"), nullable=False)
    raw = Column(JSON, nullable=False)
    score = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    farmer = relationship("Farmer")

class RiskResult(Base):
    __tablename__ = "risk_results"
    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=False)
    perfios_id = Column(Integer, ForeignKey("perfios_results.id"), nullable=True)
    onevigil_id = Column(Integer, ForeignKey("onevigil_results.id"), nullable=True)
    combined_score = Column(Float, nullable=True)
    details = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
