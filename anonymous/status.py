from locust import task, between
from anonymous.baseAnonymous import BaseAnonymous
from config import BASE_URL

class checkStatus(BaseAnonymous):

    wait_time = between(1, 2)
    host = BASE_URL

    @task
    def get_orders(self):
        self.client.get("/api/status", headers=self.headers)
