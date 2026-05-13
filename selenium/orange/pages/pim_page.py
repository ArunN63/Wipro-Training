from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class PIMPage(BasePage):
    # Locators
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button')][contains(., 'Add')]")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    MIDDLE_NAME_INPUT = (By.NAME, "middleName")
    EMPLOYEE_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'oxd-toast')]//p[contains(text(), 'Success')]")
    EMPLOYEE_LIST_TAB = (By.XPATH, "//a[contains(text(), 'Employee List')]")
    EMPLOYEE_SEARCH_INPUT = (By.XPATH, "//div[contains(@class, 'oxd-autocomplete-text-input')]/input")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button--ghost')]")
    DELETE_BUTTON = (By.XPATH, "//i[contains(@class, 'oxd-icon-trash')]")
    CONFIRM_DELETE = (By.XPATH, "//button[contains(text(), 'Yes, Delete')]")

    def click_add_employee(self):
        """Click Add Employee button"""
        self.click(self.ADD_EMPLOYEE_BUTTON)
        return self

    def add_employee(self, first_name, last_name, middle_name=""):
        """Add a new employee"""
        self.logger.info(f"Adding employee: {first_name} {last_name}")
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        if middle_name:
            self.send_keys(self.MIDDLE_NAME_INPUT, middle_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        return self

    def click_save(self):
        """Click Save button with explicit wait"""
        save_button = self.wait_for_element_clickable(self.SAVE_BUTTON)
        save_button.click()
        time.sleep(2)
        return self

    def get_success_message(self):
        """Get success message text"""
        message = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return message.text

    def search_employee(self, employee_name):
        """Search for an employee"""
        self.click(self.EMPLOYEE_LIST_TAB)
        time.sleep(1)
        search_input = self.find(self.EMPLOYEE_SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(employee_name)
        time.sleep(2)
        self.click(self.SEARCH_BUTTON)
        time.sleep(2)
        return self

    def is_employee_in_list(self, first_name, last_name):
        """Check if employee exists in list"""
        full_name = f"{first_name} {last_name}"
        try:
            employee_locator = (By.XPATH, f"//div[contains(text(), '{full_name}')]")
            return self.find(employee_locator).is_displayed()
        except:
            return False

    def get_employee_count(self):
        """Get number of employees in list"""
        employees = self.find_elements((By.XPATH, "//div[contains(@class, 'oxd-table-card')]"))
        return len(employees)