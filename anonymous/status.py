from locust import task
from anonymous.baseAnonymous import BaseAnonymous

class checkStatus(BaseAnonymous):

    @task
    def check_health_status(self):
        response = self.client.get("/api/status", headers=self.headers)
        assert response.status_code == 200, f"Error: Expected status code 200, but got {response.status_code}"
        assert response.json() is True, f"Error: Expected 'true' in response body, but got {response.json()}"
