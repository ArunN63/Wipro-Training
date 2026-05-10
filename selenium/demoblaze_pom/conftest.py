import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import logging
import os
from datetime import datetime
import allure
from allure_commons.types import AttachmentType

from config import BASE_URL, SCREENSHOTS_DIR


# Configure logging
def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    log_filename = f"logs/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """Setup WebDriver for Microsoft Edge - VM/Laptop compatible"""
    setup_logging()

    # Simple Edge configuration that works on most VMs
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-gpu")  # Important for VMs
    options.add_argument("--no-sandbox")  # Important for VMs
    options.add_argument("--disable-dev-shm-usage")  # Important for VMs

    # Use Service without specifying path (assumes Edge driver is in PATH)
    # If Edge driver is not in PATH, you'll need to specify the path
    service = Service()

    try:
        driver = webdriver.Edge(service=service, options=options)
        driver.get(BASE_URL)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    except Exception as e:
        print(f"Error initializing Edge driver: {e}")
        print("\nTroubleshooting steps:")
        print("1. Make sure Microsoft Edge is installed")
        print("2. Download Edge WebDriver from: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
        print("3. Place msedgedriver.exe in your project folder or add to PATH")
        raise


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            if not os.path.exists(SCREENSHOTS_DIR):
                os.makedirs(SCREENSHOTS_DIR)
            screenshot_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)
            driver.save_screenshot(screenshot_path)

            # Attach to Allure report
            allure.attach.file(
                screenshot_path,
                name=f"Failed Test Screenshot - {item.name}",
                attachment_type=AttachmentType.PNG
            )

            # Also attach page source
            allure.attach(
                driver.page_source,
                name="Page Source on Failure",
                attachment_type=AttachmentType.HTML
            )


def pytest_configure(config):
    """Configure pytest"""
    if not os.path.exists(SCREENSHOTS_DIR):
        os.makedirs(SCREENSHOTS_DIR)
    if not os.path.exists("logs"):
        os.makedirs("logs")