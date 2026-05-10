from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = logging.getLogger(__name__)

    def click(self, by_locator):
        """Click on an element"""
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

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

    def wait_for_alert(self):
        """Wait for alert to be present"""
        return self.wait.until(EC.alert_is_present())