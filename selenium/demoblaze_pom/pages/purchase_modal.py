from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class PurchaseModal(BasePage):
    NAME_FIELD = (By.ID, "name")
    COUNTRY_FIELD = (By.ID, "country")
    CITY_FIELD = (By.ID, "city")
    CARD_FIELD = (By.ID, "card")
    MONTH_FIELD = (By.ID, "month")
    YEAR_FIELD = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(), 'Purchase')]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".sweet-alert h2")
    OK_BUTTON = (By.XPATH, "//button[contains(text(), 'OK')]")

    def fill_purchase_form(self, data_dict):
        """Fill the purchase form with data dictionary"""
        with allure.step(f"Fill name: {data_dict.get('name', '')}"):
            self.send_keys(self.NAME_FIELD, data_dict.get('name', ''))

        with allure.step(f"Fill country: {data_dict.get('country', '')}"):
            self.send_keys(self.COUNTRY_FIELD, data_dict.get('country', ''))

        with allure.step(f"Fill city: {data_dict.get('city', '')}"):
            self.send_keys(self.CITY_FIELD, data_dict.get('city', ''))

        with allure.step(f"Fill card: {data_dict.get('card', '')}"):
            self.send_keys(self.CARD_FIELD, data_dict.get('card', ''))

        with allure.step(f"Fill month: {data_dict.get('month', '')}"):
            self.send_keys(self.MONTH_FIELD, data_dict.get('month', ''))

        with allure.step(f"Fill year: {data_dict.get('year', '')}"):
            self.send_keys(self.YEAR_FIELD, data_dict.get('year', ''))

        return self

    def click_purchase(self):
        """Click Purchase button"""
        self.click(self.PURCHASE_BUTTON)
        return self

    def get_success_message(self):
        """Get success message after purchase"""
        return self.get_text(self.SUCCESS_MESSAGE)