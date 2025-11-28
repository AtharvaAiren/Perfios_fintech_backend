import time
from app.config import settings

class PerfiosClient:
    def __init__(self):
        self.base = settings.PERFIOS_API_URL
        self.api_key = settings.PERFIOS_API_KEY

    def upload_and_parse(self, file_path: str):
        time.sleep(1)
        return {
            "summary": {
                "average_monthly_credit": 25000,
                "average_monthly_debit": 18000,
                "income_stability": "moderate"
            },
            "risk_score": 0.35,
            "raw_text": "parsed transactions..."
        }
