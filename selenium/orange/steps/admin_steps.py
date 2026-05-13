from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AdminSteps:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_admin(self):
        """Navigate to Admin module"""
        admin_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
        admin_link.click()
        return self

    def search_with_criteria(self, datatable):
        """Exercise 3: Accept DataTable object and iterate through dictionary"""
        # Parse the data table
        headers = datatable.rows[0].cells
        values = datatable.rows[1].cells

        # Create dictionary from data table
        search_criteria = {}
        for i in range(len(headers)):
            search_criteria[headers[i].lower()] = values[i]

        # Fill search fields based on dictionary
        if search_criteria.get('username'):
            username_field = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-input-group')]/div/input")))
            username_field.send_keys(search_criteria['username'])

        if search_criteria.get('user role'):
            # Click user role dropdown
            role_dropdown = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'oxd-select-text')]")[0]
            role_dropdown.click()
            time.sleep(1)
            role_option = self.driver.find_element(By.XPATH,
                                                   f"//div[@role='option']//span[text()='{search_criteria['user role']}']")
            role_option.click()

        if search_criteria.get('status'):
            # Click status dropdown
            status_dropdown = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'oxd-select-text')]")[1]
            status_dropdown.click()
            time.sleep(1)
            status_option = self.driver.find_element(By.XPATH,
                                                     f"//div[@role='option']//span[text()='{search_criteria['status']}']")
            status_option.click()

        # Click search button
        search_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_btn.click()
        time.sleep(2)
        return self

    def get_result_count(self):
        """Get number of search results"""
        results = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'oxd-table-card')]")
        return len(results)


# BDD step implementations
@given("I navigate to Admin module")
def navigate_to_admin(driver):
    admin_steps = AdminSteps(driver)
    admin_steps.navigate_to_admin()


@when("I enter the following search criteria:")
def search_with_data_table(driver, datatable):
    admin_steps = AdminSteps(driver)
    admin_steps.search_with_criteria(datatable)


@then("I should see at least 1 result")
def verify_results(driver):
    admin_steps = AdminSteps(driver)
    result_count = admin_steps.get_result_count()
    assert result_count > 0, f"Expected at least 1 result, got {result_count}"