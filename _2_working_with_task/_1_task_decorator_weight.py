from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com/"

    @task(2)
    def login_URL(self):
        print("I am logging into URL")

    @task(4)
    def logout_URL(self):
        print("I am logging out URL")
