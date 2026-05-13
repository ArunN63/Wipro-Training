from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time


class AdminPage(BasePage):
    # Locators
    USERNAME_FILTER = (By.XPATH, "//div[contains(@class, 'oxd-input-group')]/div/input")
    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'oxd-select-text')])[1]")
    STATUS_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'oxd-select-text')])[2]")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button--ghost')]")
    TABLE_ROWS = (By.XPATH, "//div[contains(@class, 'oxd-table-card')]")

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
        # Implementation depends on table structure
        # This is a simplified version
        return self.get_search_results_count() > 0