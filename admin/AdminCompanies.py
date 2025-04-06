
from locust import task, between
from baseAdmin import BaseAdmin
from config import BASE_URL

class AdminCompanies(BaseAdmin):
    wait_time = between(1, 3)
    host = BASE_URL

    @task
    def get_company_premium(self):
        self.client.get("/api/companies/premium", headers=self.headers)
