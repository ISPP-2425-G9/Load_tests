import random
from locust import task
from customer.baseCustomerPremium import BaseCustomerPremium


class CustomerPremiumMessages(BaseCustomerPremium):

    @task
    def get_valid_messages(self):
        customer_id = self.id
        self.client.get(f"/api/messages/{customer_id}/my_messages", headers=self.headers, catch_response=True)

    @task
    def get_valid_message(self):
        message_id = random.randint(5, 6)
        self.client.get(f"/api/messages/{message_id}", headers=self.headers, catch_response=True)
