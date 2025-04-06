from locust import task, between
from baseCompany import BaseCompany
from config import BASE_URL

class AdminUserTest(BaseCompany):
    wait_time = between(1, 3)
    host = BASE_URL

    @task
    def get_company_by_id(self):
        company_id = self.id
        self.client.get(f"/api/auth/companies/{company_id}", headers=self.headers)
