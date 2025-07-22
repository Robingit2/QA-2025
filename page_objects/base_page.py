from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        self.driver.get(url)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    # def scroll_to(self, locator):
    #     el = self.find(locator)
    #     self.driver.execute_script("arguments[0].scrollIntoView();", el)
    def scroll_to(self, locator, timeout=100):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)



