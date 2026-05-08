from selenium.webdriver.common.by import By


class PersonalDetailsPage:

    personal_heading = (By.XPATH, "//h6[text()='Personal Details']")

    def __init__(self, driver):
        self.driver = driver

    def is_personal_page_opened(self):
        return self.driver.find_element(*self.personal_heading).is_displayed()