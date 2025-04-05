import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_URL", "http://localhost:8080")
