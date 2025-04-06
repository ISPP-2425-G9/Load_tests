from locust import task
from baseCustomerPremium import BaseCustomerPremium

class CustomerDeathCertificates(BaseCustomerPremium):

    @task
    def get_obituary_by_id(self):
        obituary_id = self.obituary_id
        self.client.get(f"/api/deathCertificate/obituary/{obituary_id}", headers=self.headers, catch_response=True)
