from locust import HttpUser, task, between


class MyWebUser(HttpUser):
    wait_time = between(1, 2)
    weight = 3
    host = "http://newtours.demoaut.com/"

    @task
    def login_URL(self):
        print(datetime.now())


class MyMobileUser(HttpUser):
    wait_time = between(1, 2)
    weight = 1
    host = "http://newtours.demoaut.com/"

    @task
    def login_URL(self):
        print(datetime.now())
