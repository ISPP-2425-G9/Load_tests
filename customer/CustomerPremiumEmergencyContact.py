from locust import task
from baseCustomerPremium import BaseCustomerPremium

class CustomerCompanies(BaseCustomerPremium):

    @task
    def get_valid_contacts(self):
        self.client.get("/api/contacts", headers=self.headers, catch_response=True)
