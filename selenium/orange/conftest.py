import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os
from datetime import datetime


@pytest.fixture(scope="function")
def driver():
    """Setup WebDriver for Microsoft Edge using local driver"""

    # Path to local Edge driver - UPDATE THIS PATH
    edge_driver_path = r"C:\wipro training\selenium\orange\msedgedriver.exe"

    # If not found, try current directory
    if not os.path.exists(edge_driver_path):
        edge_driver_path = "msedgedriver.exe"

    if not os.path.exists(edge_driver_path):
        raise Exception(f"Edge driver not found! Please download from: "
                        f"https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")

    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed if hasattr(request.node, 'rep_call') else False:
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"failure_{request.node.name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\n✓ Screenshot saved: {screenshot_path}")