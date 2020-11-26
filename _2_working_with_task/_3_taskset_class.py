from locust import HttpUser, task, between, TaskSet


class UserBehaviour(TaskSet):
    @task()
    def add_cart(userclass):
        print("I am add to cart")

    @task()
    def view_product(userclass):
        print("I am view product")


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com/"
    task = [UserBehaviour]
