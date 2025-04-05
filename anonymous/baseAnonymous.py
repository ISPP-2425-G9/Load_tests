from locust import HttpUser

class BaseAnonymous(HttpUser):
    abstract = True

    def on_start(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
