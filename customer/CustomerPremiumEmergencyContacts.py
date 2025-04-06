from locust import task
from customer.baseCustomerPremium import BaseCustomerPremium


class CustomerPremiumEmergencyContacts(BaseCustomerPremium):

    @task
    def get_valid_contacts(self):
        self.client.get("/api/contacts", headers=self.headers, catch_response=True)
