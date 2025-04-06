from locust import task
from baseCustomer import BaseCustomer

class CustomerTemplates(BaseCustomer):

    @task
    def get_templates(self):
        self.client.get("/api/templates/urls", headers=self.headers)
