from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task(2)
    def load_courses_page(self):
        # Visit the courses listing page
        self.client.get("/courses", name="/courses")

    @task(3)
    def search_course(self):
        # Search for 'QA' courses using the search query param
        self.client.get("/courses?q=QA", name="/courses?q=QA")

    @task(1)
    def course_detail(self):
        # Visit a specific course detail page
        self.client.get("/courses/quality-assurance-training-in-nepal", name="/courses/quality-assurance-training-in-nepal")

class WebsiteUser(HttpUser):
    host = "https://www.mindrisers.com.np"
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # Simulates user think time between actions
