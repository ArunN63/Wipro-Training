from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[contains(text(), 'Add to cart')]")

    def add_product_to_cart(self):
        """Add product to cart and handle alert"""
        self.logger.info("Clicking 'Add to cart' button")
        self.click(self.ADD_TO_CART_BUTTON)

        # Wait for alert and accept it
        alert = self.wait_for_alert()
        alert_text = alert.text
        self.logger.info(f"Alert appeared with text: {alert_text}")
        alert.accept()
        self.logger.info("Alert accepted successfully")

        return self