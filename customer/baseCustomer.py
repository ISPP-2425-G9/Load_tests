from locust import HttpUser, between
from config import BASE_URL, CLIENT_EMAIL, CLIENT_PASSWORD

class BaseCustomer(HttpUser):
    abstract = True
    wait_time = between(1, 2)
    host = BASE_URL

    def on_start(self):
        res = self.client.post("/api/auth/login", json={"id": CLIENT_EMAIL, "password": CLIENT_PASSWORD})
        self.token = res.json().get("token")
        self.id = res.json().get("id")
        self.headers = {"Authorization": f"Bearer {self.token}"}
