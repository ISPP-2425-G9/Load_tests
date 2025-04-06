from locust import HttpUser, between
from config import BASE_URL, CLIENT_PREMIUM_EMAIL, CLIENT_PREMIUM_PASSWORD

class BaseCustomerPremium(HttpUser):
    abstract = True
    wait_time = between(1, 2)
    host = BASE_URL

    def on_start(self):
        res = self.client.post("/api/auth/login", json={"id": CLIENT_PREMIUM_EMAIL, "password": CLIENT_PREMIUM_PASSWORD})
        self.token = res.json().get("token")
        self.id = res.json().get("id")
        self.headers = {"Authorization": f"Bearer {self.token}"}
