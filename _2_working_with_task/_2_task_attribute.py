from locust import HttpUser, task, between


def login_URL(userclass):
    print("I am logging into URL")


def logout_URL(userclass):
    print("I am logging out URL")


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com/"
    task = {login_URL: 3, logout_URL: 2}
