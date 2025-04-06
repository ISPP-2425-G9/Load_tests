import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_URL", "http://localhost:8080")

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin1@caronte.site")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")

CLIENT_EMAIL = os.getenv("CLIENT_EMAIL", "cliente1@caronte.site")
CLIENT_PASSWORD = os.getenv("CLIENT_PASSWORD", "customer")

CLIENT_PREMIUM_EMAIL = os.getenv("CLIENT_EMAIL", "cliente2@caronte.site")
CLIENT_PREMIUM_PASSWORD = os.getenv("CLIENT_PASSWORD", "customer")

COMPANY_EMAIL = os.getenv("COMPANY_EMAIL", "empresa1@caronte.site")
COMPANY_PASSWORD = os.getenv("COMPANY_PASSWORD", "company")
