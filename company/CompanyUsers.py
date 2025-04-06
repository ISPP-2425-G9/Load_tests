from locust import task
from baseCompany import BaseCompany

class CompanyUsers(BaseCompany):

    @task
    def get_company_by_id(self):
        company_id = self.id
        self.client.get(f"/api/auth/companies/{company_id}", headers=self.headers)
