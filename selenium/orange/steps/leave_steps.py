from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


class LeaveSteps:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.initial_balance = 0

    def navigate_to_leave(self):
        """Navigate to Leave module"""
        leave_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']")))
        leave_link.click()
        return self

    def click_apply_leave(self):
        """Click Apply Leave button"""
        apply_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'oxd-button')][contains(., 'Apply')]")))
        apply_btn.click()
        return self

    def select_leave_type(self, leave_type):
        """Select leave type"""
        type_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'oxd-select-text')]")))
        type_dropdown.click()
        time.sleep(1)
        option = self.driver.find_element(By.XPATH, f"//div[@role='option']//span[text()='{leave_type}']")
        option.click()
        return self

    def select_date(self, from_date, to_date):
        """Select from and to dates"""
        from_input = self.driver.find_element(By.XPATH, "//input[@placeholder='yyyy-mm-dd']")
        from_input.clear()
        from_input.send_keys(from_date)

        to_input = self.driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-mm-dd']")[1]
        to_input.clear()
        to_input.send_keys(to_date)
        return self

    def click_apply(self):
        """Click Apply button"""
        apply_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        apply_btn.click()
        time.sleep(2)
        return self

    def get_initial_leave_balance(self):
        """Exercise 4: Store initial leave balance as integer"""
        leave_balance_text = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'leave-balance')]//p"))).text
        # Extract number from text (e.g., "Balance: 8.00" -> 8.00)
        numbers = re.findall(r'\d+\.?\d*', leave_balance_text)
        self.initial_balance = float(numbers[0]) if numbers else 0
        return self.initial_balance

    def get_final_leave_balance(self):
        """Get final leave balance after application"""
        leave_balance_text = self.driver.find_element(By.XPATH, "//div[contains(@class, 'leave-balance')]//p").text
        numbers = re.findall(r'\d+\.?\d*', leave_balance_text)
        final_balance = float(numbers[0]) if numbers else 0
        return final_balance

    def verify_balance_reduction(self, days_deducted=1):
        """Exercise 4: Compare initial and final balance to ensure deduction"""
        final_balance = self.get_final_leave_balance()
        expected_balance = self.initial_balance - days_deducted
        assert final_balance == expected_balance, f"Expected balance {expected_balance}, got {final_balance}"
        return True

    def get_success_toast_message(self):
        """Exercise 4: Capture success toast message text"""
        toast = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast')]//p")))
        return toast.text


# BDD step implementations
@given("I navigate to Leave module")
def navigate_to_leave(driver):
    leave_steps = LeaveSteps(driver)
    leave_steps.navigate_to_leave()


@when("I click on Apply Leave")
def click_apply_leave(driver):
    leave_steps = LeaveSteps(driver)
    leave_steps.click_apply_leave()


@when(parsers.parse('I select "{leave_type}" as leave type'))
def select_leave_type(driver, leave_type):
    leave_steps = LeaveSteps(driver)
    leave_steps.select_leave_type(leave_type)


@when(parsers.parse('I select from date "{from_date}" to date "{to_date}"'))
def select_dates(driver, from_date, to_date):
    leave_steps = LeaveSteps(driver)
    leave_steps.select_date(from_date, to_date)
    # Store initial balance before applying
    leave_steps.get_initial_leave_balance()


@when("I click Apply button")
def click_apply(driver):
    leave_steps = LeaveSteps(driver)
    leave_steps.click_apply()


@then(parsers.parse('I should see success toast message "{expected_message}"'))
def verify_toast(driver, expected_message):
    leave_steps = LeaveSteps(driver)
    actual_message = leave_steps.get_success_toast_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"


@then("my leave balance should be reduced by 1 day")
def verify_balance(driver):
    leave_steps = LeaveSteps(driver)
    assert leave_steps.verify_balance_reduction(1) == True