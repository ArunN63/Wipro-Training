from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time


class AdminPage(BasePage):
    # Locators
    USERNAME_FILTER = (By.XPATH, "//div[contains(@class, 'oxd-input-group')]/div/input")
    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'oxd-select-text')])[1]")
    STATUS_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'oxd-select-text')])[2]")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button--ghost')]")
    ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button')][contains(., 'Add')]")
    TABLE_ROWS = (By.XPATH, "//div[contains(@class, 'oxd-table-card')]")
    TABLE_CELLS = (By.XPATH, "//div[contains(@class, 'oxd-table-card')]//div[contains(@class, 'oxd-table-cell')]")

    def search_users_with_criteria(self, username="", user_role="", status=""):
        """Search users using multiple criteria"""
        self.logger.info(f"Searching with criteria - Username: {username}, Role: {user_role}, Status: {status}")

        if username:
            self.send_keys(self.USERNAME_FILTER, username)
            time.sleep(1)

        if user_role:
            self.click(self.USER_ROLE_DROPDOWN)
            time.sleep(1)
            role_option = (By.XPATH, f"//div[@role='option']//span[text()='{user_role}']")
            self.click(role_option)
            time.sleep(1)

        if status:
            self.click(self.STATUS_DROPDOWN)
            time.sleep(1)
            status_option = (By.XPATH, f"//div[@role='option']//span[text()='{status}']")
            self.click(status_option)
            time.sleep(1)

        self.click(self.SEARCH_BUTTON)
        time.sleep(2)
        return self

    def get_search_results_count(self):
        """Get number of search results"""
        results = self.find_elements(self.TABLE_ROWS)
        return len(results)

    def verify_search_results(self, expected_username="", expected_role="", expected_status=""):
        """Verify search results match criteria"""
        return self.get_search_results_count() > 0

    def clear_filters(self):
        """Clear all search filters"""
        self.click(self.RESET_BUTTON)
        time.sleep(1)
        return self