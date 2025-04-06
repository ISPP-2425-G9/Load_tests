from locust import task
from admin.baseAdmin import BaseAdmin
import random

class AdminUsers(BaseAdmin):

    @task
    def get_customers(self):
        self.client.get("/api/auth/admin/customers", headers=self.headers)

    @task
    def get_customer_by_id(self):
        customer_id = random.randint(5, 6)
        self.client.get(f"/api/auth/admin/customers/{customer_id}", headers=self.headers)

    @task
    def get_companies(self):
        self.client.get("/api/auth/admin/companies", headers=self.headers)

    @task
    def get_company_by_id(self):
        company_id = random.randint(7, 38)
        self.client.get(f"/api/auth/admin/companies/{company_id}", headers=self.headers)
