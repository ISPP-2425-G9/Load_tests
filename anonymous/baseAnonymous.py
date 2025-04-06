from locust import HttpUser, between
from config import BASE_URL

class BaseAnonymous(HttpUser):
    abstract = True
    wait_time = between(1, 2)
    host = BASE_URL

    def on_start(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
