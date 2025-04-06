import random
from locust import task
from baseCustomerPremium import BaseCustomerPremium

class CustomerDeathCertificate(BaseCustomerPremium):

    @task
    def get_obituary_by_id(self):
        obituary_id = random.randint(1, 2)
        self.client.get(f"/api/deathCertificate/obituary/{obituary_id}", headers=self.headers, catch_response=True)
