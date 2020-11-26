from locust import HttpUser, task, between


class MyUser(HttpUser):

    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com"

    @task
    def launch_URL(self):
        self.client.get("/mercurysignon.php", name="launchmercury")

    @task
    def login(self):
        login_data = {"action": "process",
                      "userName": "qamile1@gmail.com", "password": "qamile"}
        self.client.post("/test/newtours/index.php",
                         name="login", data=login_data)
