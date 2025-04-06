import random
from locust import task
from baseCustomerPremium import BaseCustomerPremium

class CustomerPremiumMessages(BaseCustomerPremium):

    @task
    def get_valid_messages(self):
        customer_id = self.id
        with self.client.get(f"/api/messages/{customer_id}/my_messages", headers=self.headers, catch_response=True) as response:
            if response.status_code >= 400:
                response.success()
            else:
                response.failure(f"Expected error but got {response.status_code}")

    @task
    def get_valid_message(self):
        message_id = random.randint(5, 6)
        self.client.get(f"/api/messages/{message_id}", headers=self.headers, catch_response=True)
