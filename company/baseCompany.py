from locust import HttpUser
from config import COMPANY_EMAIL, COMPANY_PASSWORD

class BaseCompany(HttpUser):
    abstract = True

    def on_start(self):
        res = self.client.post("/api/auth/login", json={"id": COMPANY_EMAIL, "password": COMPANY_PASSWORD})
        self.token = res.json().get("token")
        self.headers = {"Authorization": f"Bearer {self.token}"}
