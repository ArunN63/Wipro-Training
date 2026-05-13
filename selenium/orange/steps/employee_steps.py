from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EmployeeSteps:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_pim(self):
        """Navigate to PIM module"""
        pim_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_link.click()
        return self

    def click_add_employee(self):
        """Click Add Employee button"""
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'oxd-button')][contains(., 'Add')]")))
        add_btn.click()
        return self

    def enter_name(self, first_name, last_name):
        """Exercise 2: Dynamically picks up values from Examples table"""
        # Explicit wait for first name field
        first_name_field = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.NAME, "lastName")
        last_name_field.send_keys(last_name)
        return self

    def click_save_button(self):
        """Exercise 2: Explicit Wait to ensure Save button is clickable"""
        # Synchronization step - wait for Save button to be clickable
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        save_button.click()
        time.sleep(2)  # Wait for save to complete
        return self

    def get_success_message(self):
        """Get success message text"""
        success_msg = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'oxd-toast')]//p[contains(text(), 'Success')]")))
        return success_msg.text


# BDD step implementations
@given("I navigate to PIM module")
def navigate_to_pim(driver):
    employee_steps = EmployeeSteps(driver)
    employee_steps.navigate_to_pim()


@when("I click on Add Employee button")
def click_add_employee(driver):
    employee_steps = EmployeeSteps(driver)
    employee_steps.click_add_employee()


@when(parsers.parse('I enter "{first_name}" and "{last_name}"'))
def enter_employee_name(driver, first_name, last_name):
    employee_steps = EmployeeSteps(driver)
    employee_steps.enter_name(first_name, last_name)


@when("I click Save button")
def click_save(driver):
    employee_steps = EmployeeSteps(driver)
    employee_steps.click_save_button()


@then(parsers.parse('I should see success message "{expected_message}"'))
def verify_success(driver, expected_message):
    employee_steps = EmployeeSteps(driver)
    actual_message = employee_steps.get_success_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"