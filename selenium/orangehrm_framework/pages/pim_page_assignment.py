from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.personal_detail_page_assignment import PersonalDetailsPage


class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def view_employee_details(self, employee_name):

        employee_xpath = (
            f"//div[contains(text(),'{employee_name}')]"
        )

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, employee_xpath))
        )

        self.driver.find_element(By.XPATH, employee_xpath).click()

        return PersonalDetailsPage(self.driver)