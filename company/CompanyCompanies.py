from locust import task
from company.baseCompany import BaseCompany


class CompanyCompanies(BaseCompany):

    @task
    def get_company_types(self):
        self.client.get("/api/companies/companiesTypes", headers=self.headers)

    @task
    def get_company_premium(self):
        self.client.get("/api/companies/premium", headers=self.headers)
