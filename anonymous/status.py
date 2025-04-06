from locust import task, between
from anonymous.baseAnonymous import BaseAnonymous
from config import BASE_URL

class checkStatus(BaseAnonymous):

    wait_time = between(1, 2)
    host = BASE_URL

    @task
    def check_health_status(self):
        response = self.client.get("/api/status", headers=self.headers)
        assert response.status_code == 200, f"Error: Expected status code 200, but got {response.status_code}"
        assert response.json() is True, f"Error: Expected 'true' in response body, but got {response.json()}"
