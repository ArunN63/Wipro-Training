import pytest

from pages.loginpage import LoginPage
from pages.inventorypage import InventoryPage
from utils.csv_reader import CSVReader
from utils.excel_reader import ExcelReader

@pytest.mark.parametrize(
    "data",
    # CSVReader.read_csv("product_validation_data.csv")
    ExcelReader.read_excel("test_data.xlsx", "product_validation_data")
)
@pytest.mark.order(4)
def test_product_data(driver, data):
    # Arrange: login is setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Action: Login
    login_page.login()
    product_names = inventory_page.get_product_names()

    # Assert: inventory page contract
    #After DDT
    assert data["product_name"] in product_names, '1 or more Product names are not in the inventory'

@pytest.mark.order(5)
def test_logout(driver):
    # Arrange: login is setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Action: Login
    login_page.login()
    inventory_page.logout()

    assert "saucedemo.com" in driver.current_url
