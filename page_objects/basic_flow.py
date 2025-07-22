from selenium.webdriver.common.by import By

from .base_page import BasePage
import time
import random
class BasicFlow(BasePage):
    URL = "https://www.mindrisers.com.np/"
    # COURSES = (By.XPATH, "//a[contains(text(),'our courses')]")
    # CONTACT_US_SECTION = (By.XPATH, "//a[normalize-space()='contact us']")
    # TESTIMONIAL_SECTION = (
    #     By.XPATH,
    #     "//section[contains(@class, 'section-wrapper-m') and contains(@style, 'testimonials/stroke-bg.svg')]"
    # )
    FOOTER = (By.XPATH, "//footer[contains(@class, 'bg-primary')]")
    COURSE_SECTION = (By.XPATH, "//section[contains(@class, 'section-wrapper-m-sm')]")
    VIEW_ALL = (By.XPATH, "//div[contains(@class, 'flex justify-end')]//a[.//span[text()='view All']]")

    SECTION_WRAPPER_M = (By.XPATH, "//section[contains(@class, 'section-wrapper-m')]")
    SEARCH_INPUT = (By.XPATH, "//input[@name='searchTerm']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn-simple")
    SEARCH_RESULTS = (By.XPATH, "//section[1]")
    
    COURSE_LEARN_MORE = (By.XPATH, "//section[1]//div[2]//div[1]//ul[1]//li[1]//a[1]//div[1]//span[1]")
    QUICK_INQUIRY_FORM = (By.XPATH, "//form[@id='quick_inquiry']")

    def load(self):
        self.go(self.URL)

    # def scroll_testimonials(self):
    #     self.scroll_to(self.TESTIMONIAL_SECTION)
    #     time.sleep(5) 

    

    def basic_flow(self):
        footer = self.driver.find_element(*self.FOOTER)
        self.slow_scroll_to_element(footer)
        time.sleep(2)

        course_section = self.driver.find_element(*self.COURSE_SECTION)
        self.slow_scroll_to_element(course_section)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(0.5)
        self.click(self.VIEW_ALL)
        time.sleep(4)
        self.scroll_to_last_visible_in_section()
        self.scroll_to_search_and_search("Machine Learning")
        
        
    def scroll_to_last_visible_in_section(self):
        section = self.driver.find_element(*self.SECTION_WRAPPER_M)
        last_child = self.driver.execute_script(
            "return arguments[0].lastElementChild;", section
        )
        self.slow_scroll_to_element(last_child)
        time.sleep(1)
        
    def scroll_to_search_and_search(self, text):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        self.slow_scroll_to_element(search_input)
        time.sleep(1)
        search_input.clear()
        search_input.send_keys(text)
        time.sleep(0.5)

        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
        time.sleep(2)
        self.scroll_above_footer()
    
    def scroll_above_footer(self):
        footer = self.driver.find_element(*self.FOOTER)
        footer_y = footer.location['y']
        scroll_to = max(footer_y - 400, 0)
        self.driver.execute_script(f"window.scrollTo(0, {scroll_to});")
        time.sleep(4) 
        search_results = self.driver.find_element(*self.SEARCH_RESULTS)
        self.slow_scroll_to_element(search_results)
        time.sleep(4)
        self.click(self.COURSE_LEARN_MORE)
        time.sleep(4)
        self.submit_form_query()
        
    def submit_form_query(self):
        form = self.driver.find_element(*self.QUICK_INQUIRY_FORM)
        self.slow_scroll_to_element(form)
        # self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", form)
        time.sleep(1)
        
        self.driver.find_element(By.NAME, "name").send_keys("John Doe")
        self.driver.find_element(By.NAME, "email").send_keys("john@example.com")
        self.driver.find_element(By.NAME, "mobile_no").send_keys("9800000000")
        self.driver.find_element(By.NAME, "subject").send_keys("Enquiry about course")
        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(1)
        select_element = self.driver.find_element(By.NAME, "select_course")
        # select = Select(select_element)
        # select.select_by_value("5")
        select_element.click()
        time.sleep(1)
        option = self.driver.find_element(By.XPATH, "//select[@name='select_course']/option[@value='5']")
        option.click()
        
        self.driver.find_element(By.NAME, "message").send_keys("I am interested in this course.")

        # submit_btn = self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Submit Enquiry')]")
        # submit_btn.click()

        time.sleep(6)

    
    def slow_scroll_to_element(self, element):
        y = element.location['y']
        current = self.driver.execute_script("return window.pageYOffset;")
        step = 10

        if current < y:
            # Scroll down
            while current < y:
                current += step
                if current > y:
                    current = y
                self.driver.execute_script(f"window.scrollTo(0, {current});")
                time.sleep(0.01)
        else:
            # Scroll up
            while current > y:
                current -= step
                if current < y:
                    current = y
                self.driver.execute_script(f"window.scrollTo(0, {current});")
                time.sleep(0.01)

        time.sleep(0.5)


        


