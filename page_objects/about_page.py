from .base_page import BasePage

class AboutPage(BasePage):
    def verify_url(self):
        return "about" in self.driver.current_url
