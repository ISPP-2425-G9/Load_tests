from locust import task, between
from baseCompany import BaseCompany
from config import BASE_URL

class CompanyTypeTest(BaseCompany):
    wait_time = between(1, 2)
    host = BASE_URL

    @task
    def get_company_types(self):
        self.client.get("/api/companies/companiesTypes", headers=self.headers)
