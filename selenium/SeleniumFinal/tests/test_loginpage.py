import pytest

from pages.loginpage import LoginPage
from utils.csv_reader import CSVReader

from utils.excel_reader import ExcelReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil

logger = LogGen.loggen()


# @pytest.mark.order(1)
@pytest.mark.parametrize(
    "data",
    # CSVReader.read_csv("login_data.csv"),
    ExcelReader.read_excel("test_data.xlsx", "login_data")
)
def test_login(driver, data):
    login_page = LoginPage(driver)
    logger.info(f'Login page opened')
    logger.info(f'Trying to login with data - {data["username"]}, {data["password"]}')
    login_page.login(data["username"], data["password"])

    logger.info(f'Checking logged in status')
    if data["expected_result"] == "success":
        assert "inventory" in driver.current_url
        logger.info(f'Login Successful - Inventory page opened ')
        screenshot_path = ScreenshotUtil.capture_screenshot(driver, screenshot_name="login_test")

    else:
        assert "inventory" not in driver.current_url
        assert login_page.read_error_message().__contains__("Epic sadface")
        logger.error(f'Login failed -  Inventory page not opened')
        screenshot_path = ScreenshotUtil.capture_screenshot(driver, screenshot_name="login_test")