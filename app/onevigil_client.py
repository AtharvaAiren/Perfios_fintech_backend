import time
from app.config import settings

class OneVigilClient:
    def __init__(self):
        self.base = settings.ONEVIGIL_API_URL
        self.api_key = settings.ONEVIGIL_API_KEY

    def verify(self, pan: str = None, aadhaar: str = None):
        time.sleep(0.5)
        return {
            "match": True,
            "score": 0.8,
            "details": {"pan": pan, "aadhaar": aadhaar}
        }
