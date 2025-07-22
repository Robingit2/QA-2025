from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    URL = "https://www.mindrisers.com.np/contact-us"
    NAME = (By.NAME, "name")
    EMAIL = (By.NAME, "email")
    MSG = (By.NAME, "message")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR = (By.CLASS_NAME, "error")
    SUCCESS = (By.CLASS_NAME, "success")

    def load(self):
        self.go(self.URL)

    def submit_form(self, name, email, message):
        self.type(self.NAME, name)
        self.type(self.EMAIL, email)
        self.type(self.MSG, message)
        self.click(self.SUBMIT)

    def get_errors(self):
        return [e.text for e in self.driver.find_elements(*self.ERROR)]

    def get_success(self):
        return self.find(self.SUCCESS).text
