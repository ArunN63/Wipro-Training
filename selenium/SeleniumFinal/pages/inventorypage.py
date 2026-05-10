from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from selenium.webdriver.support.ui import Select
from utils.logger import LogGen

logger = LogGen.loggen()

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    ADD_TO_CART_FIRST = (By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # ===== Page actions =====
    def is_loaded(self):
        logger.info(f'Checking inventory page laod')
        return self.is_visible(self.INVENTORY_CONTAINER)

    def get_page_title(self):
        logger.info(f'Getting page title')
        return self.get_text(self.PAGE_TITLE)

    def get_products_count(self):
        logger.info(f'Getting products count')
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def add_first_product_to_cart(self):
        logger.info(f'Adding first product to cart')
        self.click(self.ADD_TO_CART_FIRST)

    def go_to_cart(self):
        logger.info(f'Going to cart')
        self.click(self.CART_ICON)

    def get_cart_count(self):
        logger.info(f'Getting cart count')
        return self.get_text(self.CART_BADGE)

    def sort_by(self, visible_text):
        logger.info(f'Sorting by : {visible_text}')
        dropdown = self.get_element(self.SORT_DROPDOWN)
        Select(dropdown).select_by_visible_text(visible_text)

    def get_product_names(self):
        logger.info(f'Getting product name')
        return [e.text for e in self.driver.find_elements(*self.PRODUCT_NAMES)]

    def logout(self):
        logger.info(f'Clicking on menu button and logout')
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_LINK)