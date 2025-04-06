from locust import HttpUser
from config import CLIENT_EMAIL, CLIENT_PASSWORD

class BaseClient(HttpUser):
    abstract = True

    def on_start(self):
        res = self.client.post("/api/auth/login", json={"id": CLIENT_EMAIL, "password": CLIENT_PASSWORD})
        self.token = res.json().get("token")
        self.headers = {"Authorization": f"Bearer {self.token}"}
