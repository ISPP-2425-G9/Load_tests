from locust import HttpUser, between
from config import BASE_URL, COMPANY_EMAIL, COMPANY_PASSWORD

class BaseCompany(HttpUser):
    abstract = True
    wait_time = between(1, 2)
    host = BASE_URL

    def on_start(self):
        res = self.client.post("/api/auth/login", json={"id": COMPANY_EMAIL, "password": COMPANY_PASSWORD})
        self.token = res.json().get("token")
        self.id = res.json().get("id")
        self.headers = {"Authorization": f"Bearer {self.token}"}
