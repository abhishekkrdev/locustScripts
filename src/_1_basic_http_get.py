from locust import HttpUser, task, between


class MyUser(HttpUser):

    wait_time = between(1, 2)
    host = "http://demo.guru99.com/"

    @task
    def launch_URL(self):
        self.client.get("/test/newtours/", name="viewcruise")
