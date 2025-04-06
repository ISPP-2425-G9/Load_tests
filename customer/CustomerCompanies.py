from locust import task
from baseCustomer import BaseCustomer

class CustomerCompanies(BaseCustomer):

    @task
    def get_company_types(self):
        self.client.get("/api/companies/companiesTypes", headers=self.headers)

    @task
    def get_company_premium(self):
        self.client.get("/api/companies/premium", headers=self.headers)
