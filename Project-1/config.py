import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = "https://www.guvi.in"
    EXPECTED_TITLE = "HCL GUVI | Learn to code in your native language"

    BROWSER = os.getenv("TEST_BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT = 15000

    VALID_EMAIL = os.getenv("GUVI_VALID_EMAIL", "")
    VALID_PASSWORD = os.getenv("GUVI_VALID_PASSWORD", "")
    INVALID_EMAIL = "invalid_user_test@example.com"
    INVALID_PASSWORD = "WrongPassword123!"

    LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")