from locust import task
from baseCustomer import BaseCustomer

class CustomerEmergencyContacts(BaseCustomer):

    @task
    def get_invalid_contacts(self):
        with self.client.get("/api/contacts", headers=self.headers, catch_response=True) as response:
            if response.status_code >= 400:
                response.success()
            else:
                response.failure(f"Expected error but got {response.status_code}")
