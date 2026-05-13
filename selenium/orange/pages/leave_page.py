from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
import re


class LeavePage(BasePage):
    # Locators
    APPLY_LEAVE_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button')][contains(., 'Apply')]")
    LEAVE_TYPE_DROPDOWN = (By.XPATH, "//div[contains(@class, 'oxd-select-text')]")
    FROM_DATE_INPUT = (By.XPATH, "//input[@placeholder='yyyy-mm-dd']")
    TO_DATE_INPUT = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")
    COMMENT_TEXTAREA = (By.XPATH, "//textarea")
    APPLY_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class, 'oxd-toast')]//p[contains(text(), 'Success')]")
    LEAVE_BALANCE = (By.XPATH, "//div[contains(@class, 'leave-balance')]//p")
    MY_LEAVE_TAB = (By.XPATH, "//a[contains(text(), 'My Leave')]")
    LEAVE_REQUEST_TABLE = (By.XPATH, "//div[contains(@class, 'oxd-table-card')]")
    LEAVE_STATUS = (By.XPATH, "//div[contains(@class, 'oxd-table-card')]//div[contains(@class, 'oxd-table-cell')][6]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")

    def click_apply_leave(self):
        """Click on Apply Leave button"""
        self.click(self.APPLY_LEAVE_BUTTON)
        return self

    def select_leave_type(self, leave_type):
        """Select leave type from dropdown"""
        self.click(self.LEAVE_TYPE_DROPDOWN)
        time.sleep(1)
        leave_option = (By.XPATH, f"//div[@role='option']//span[text()='{leave_type}']")
        self.click(leave_option)
        return self

    def select_dates(self, from_date, to_date):
        """Select from and to dates"""
        from_input = self.find(self.FROM_DATE_INPUT)
        from_input.clear()
        from_input.send_keys(from_date)

        to_input = self.find(self.TO_DATE_INPUT)
        to_input.clear()
        to_input.send_keys(to_date)
        return self

    def add_comment(self, comment):
        """Add comment to leave application"""
        self.send_keys(self.COMMENT_TEXTAREA, comment)
        return self

    def click_apply(self):
        """Click Apply button to submit leave request"""
        self.click(self.APPLY_SUBMIT_BUTTON)
        time.sleep(2)
        return self

    def get_success_message(self):
        """Get success toast message"""
        message = self.find(self.SUCCESS_TOAST)
        return message.text

    def get_leave_balance(self):
        """Get current leave balance as float"""
        balance_element = self.find(self.LEAVE_BALANCE)
        balance_text = balance_element.text
        # Extract number from text (e.g., "8.00" from "Balance: 8.00")
        numbers = re.findall(r'\d+\.?\d*', balance_text)
        return float(numbers[0]) if numbers else 0

    def navigate_to_my_leave(self):
        """Navigate to My Leave section"""
        self.click(self.MY_LEAVE_TAB)
        time.sleep(2)
        return self

    def get_leave_status(self):
        """Get status of latest leave application"""
        status_element = self.find(self.LEAVE_STATUS)
        return status_element.text

    def get_leave_requests_count(self):
        """Get number of leave requests"""
        requests = self.find_elements(self.LEAVE_REQUEST_TABLE)
        return len(requests)