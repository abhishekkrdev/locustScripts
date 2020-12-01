from locust import HttpUser, SequentialTaskSet, task, between


class UserBehaviour(SequentialTaskSet):

    @task
    def launch_URL(self):
        with self.client.get("/", name="launchalethea", catch_response=True) as resp1:
            if("Perfecting Broadband Experience") in resp1.text:
                resp1.success()
            else:
                resp1.failure("failed to launch url")


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://alethea.in/"
    tasks = [UserBehaviour]
