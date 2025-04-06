from locust import HttpUser, between
from config import ADMIN_EMAIL, ADMIN_PASSWORD, BASE_URL

class BaseAdmin(HttpUser):
    abstract = True
    wait_time = between(1, 3)
    host = BASE_URL

    def on_start(self):
        res = self.client.post("/api/auth/login", json={"id": ADMIN_EMAIL, "password": ADMIN_PASSWORD})
        self.token = res.json().get("token")
        self.headers = {"Authorization": f"Bearer {self.token}"}
