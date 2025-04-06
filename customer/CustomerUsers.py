from locust import task
from customer.baseCustomer import BaseCustomer

class CustomerUsers(BaseCustomer):

    @task
    def get_customer_by_id(self):
        customer_id = self.id
        self.client.get(f"/api/auth/customers/{customer_id}", headers=self.headers)
