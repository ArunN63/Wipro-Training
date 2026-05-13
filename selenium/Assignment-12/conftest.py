import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging
import os
from datetime import datetime


@pytest.fixture(scope="function")
def driver():
    """Setup WebDriver for Microsoft Edge"""
    # Setup logging
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"logs/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
            logging.StreamHandler()
        ]
    )

    # Edge configuration for VM/laptop
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Fixture for logged in driver"""
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    return driver