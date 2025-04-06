from locust import task
from baseAdmin import BaseAdmin


class AdminDeathCertificate(BaseAdmin):

    @task
    def get_all_death_certificates(self):
        self.client.get("/api/deathCertificate/all", headers=self.headers)
