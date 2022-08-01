from locust import HttpUser, task


class QuickStartUser(HttpUser):
    @task
    def welcome(self):
        self.client.get("/")
