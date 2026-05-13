from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import logging
import os
from datetime import datetime


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = logging.getLogger(__name__)

    def click(self, by_locator):
        """Click on an element"""
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()
        self.logger.info(f"Clicked on element: {by_locator}")

    def find(self, by_locator):
        """Find a single element"""
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def find_elements(self, by_locator):
        """Find multiple elements"""
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def get_text(self, by_locator):
        """Get text from an element"""
        element = self.find(by_locator)
        return element.text

    def send_keys(self, by_locator, text):
        """Send keys to an element"""
        element = self.find(by_locator)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Sent keys to: {by_locator}")

    def wait_for_element_visible(self, by_locator):
        """Wait for element to be visible"""
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url

    def take_screenshot(self, name="screenshot"):
        """Take a screenshot"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join("screenshots", filename)
        self.driver.save_screenshot(filepath)
        self.logger.info(f"Screenshot saved: {filepath}")
        return filepath