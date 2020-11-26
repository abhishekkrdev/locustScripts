from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com/"

    def on_start(self):
        print('Logging In')

    @task
    def some_task(self):
        print('Some Task')

    def on_stop(self):
        print('I am logging out')
