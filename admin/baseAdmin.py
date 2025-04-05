from locust import HttpUser
from config import ADMIN_EMAIL, ADMIN_PASSWORD

class BaseAdmin(HttpUser):
    abstract = True

    def on_start(self):
        res = self.client.post("/api/login", json={"id": ADMIN_EMAIL, "password": ADMIN_PASSWORD})
        self.token = res.json().get("access_token")
        self.headers = {"Authorization": f"Bearer {self.token}"}
