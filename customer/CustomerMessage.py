from locust import task
from baseCustomer import BaseCustomer

class CustomerCompanies(BaseCustomer):

    @task
    def get_invalid_messages(self):
        customer_id = self.id
        with self.client.get(f"/{customer_id}/my_messages", headers=self.headers, catch_response=True) as response:
            if response.status_code >= 400:
                response.success()
            else:
                response.failure(f"Expected error but got {response.status_code}")