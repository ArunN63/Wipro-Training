from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class CategoryPage(BasePage):
    def __init__(self, driver, category_name):
        super().__init__(driver)
        self.category_name = category_name
        time.sleep(2)  # Wait for products to load

    # Locators
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".card-title a")

    def get_all_product_names(self):
        """Get all product names as a list of strings"""
        product_elements = self.find_elements(self.PRODUCT_ITEMS)
        product_names = [element.text for element in product_elements]
        self.logger.info(f"Found {len(product_names)} products in {self.category_name}")
        return product_names

    def verify_laptop_list_presence(self):
        """Verify that laptop list is present (not empty)"""
        product_names = self.get_all_product_names()
        assert len(product_names) > 0, "No laptops found in the list"
        self.logger.info(f"Successfully verified {len(product_names)} laptops")
        return self

    def click_product(self, product_name):
        """Click on a specific product"""
        product_locator = (By.XPATH, f"//a[contains(text(), '{product_name}')]")
        self.click(product_locator)
        from pages.product_details_page import ProductDetailsPage
        return ProductDetailsPage(self.driver)