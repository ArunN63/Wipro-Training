from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.category_page import CategoryPage


class HomePage(BasePage):
    # Locators
    LAPTOPS_CATEGORY = (By.LINK_TEXT, "Laptops")
    PHONES_CATEGORY = (By.LINK_TEXT, "Phones")
    MONITORS_CATEGORY = (By.LINK_TEXT, "Monitors")
    LOGIN_BUTTON = (By.ID, "login2")

    def click_laptops(self):
        """Click on Laptops category and return CategoryPage"""
        self.click(self.LAPTOPS_CATEGORY)
        return CategoryPage(self.driver, "Laptops")

    def click_phones(self):
        """Click on Phones category and return CategoryPage"""
        self.click(self.PHONES_CATEGORY)
        return CategoryPage(self.driver, "Phones")

    def click_monitors(self):
        """Click on Monitors category and return CategoryPage"""
        self.click(self.MONITORS_CATEGORY)
        return CategoryPage(self.driver, "Monitors")