from locust import task
from baseCustomer import BaseCustomer

class CustomerReceivers(BaseCustomer):

    @task
    def get_obituary_receivers(self):
        obituary_id = self.obituary_id
        self.client.get(f"/getReceivers/obituary/{obituary_id}", headers=self.headers)
