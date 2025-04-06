from locust import task, between
from baseAdmin import BaseAdmin
from config import BASE_URL

class DeathCertificateTest(BaseAdmin):
    wait_time = between(1, 2)
    host = BASE_URL

    @task
    def get_all_death_certificates(self):
        self.client.get("/api/deathCertificate/all", headers=self.headers)
