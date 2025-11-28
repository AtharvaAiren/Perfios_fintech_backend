from app.celery_app import celery
from app.perfios_client import PerfiosClient
from app.onevigil_client import OneVigilClient
from app.database import SessionLocal
from app import models
import time

@celery.task(bind=True)
def process_bank_statement(self, bank_statement_id: int, application_id: int = None):
    db = SessionLocal()
    try:
        bs = db.query(models.BankStatement).get(bank_statement_id)
        if not bs:
            return {"error": "bank statement not found"}

        farmer = db.query(models.Farmer).get(bs.farmer_id)

        perfios = PerfiosClient()
        onevigil = OneVigilClient()

        perfios_res = perfios.upload_and_parse(bs.file_path)
        pr = models.PerfiosResult(raw=perfios_res, summary=perfios_res.get("summary"))
        db.add(pr); db.commit(); db.refresh(pr)

        bs.perfios_result_id = pr.id
        db.add(bs); db.commit()

        ov_res = onevigil.verify(farmer.pan, farmer.aadhaar)
        ovr = models.OneVigilResult(farmer_id=farmer.id, raw=ov_res, score=ov_res.get("score"))
        db.add(ovr); db.commit(); db.refresh(ovr)

        combined = (ovr.score or 0) * 0.6 + (perfios_res.get("risk_score") or 0) * 0.4

        rr = models.RiskResult(
            application_id=application_id or 0,
            perfios_id=pr.id,
            onevigil_id=ovr.id,
            combined_score=combined,
            details={"perfios": perfios_res, "onevigil": ov_res}
        )

        db.add(rr); db.commit(); db.refresh(rr)

        if application_id:
            app = db.query(models.Application).get(application_id)
            if app:
                app.status = "completed"
                app.result = {"risk_id": rr.id, "score": rr.combined_score}
                db.add(app); db.commit()

        return {"risk_id": rr.id, "score": rr.combined_score}

    finally:
        db.close()
