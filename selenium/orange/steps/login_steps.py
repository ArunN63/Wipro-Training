from pytest_bdd import given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Exercise 1: Step Definition class for Login
class LoginSteps:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_orangehrm(self):
        """Given step: Initialize driver and navigate to URL"""
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        return self

    def enter_credentials(self, username, password):
        """When step: Accepts String username and String password as parameters"""
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        return self

    def click_login(self):
        """Click login button"""
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        return self

    def verify_url_contains_dashboard(self):
        """Then step: Assert current URL contains 'dashboard'"""
        self.wait.until(EC.url_contains("dashboard"))
        assert "dashboard" in self.driver.current_url.lower(), f"URL does not contain 'dashboard': {self.driver.current_url}"
        return True

    def get_error_message(self):
        """Get error message text"""
        error_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'alert')]")))
        return error_element.text


# BDD step implementations using the class
@given("I open OrangeHRM login page")
def open_login_page(driver):
    login_steps = LoginSteps(driver)
    login_steps.navigate_to_orangehrm()


@when(parsers.parse('I enter username "{username}" and password "{password}"'))
def enter_credentials(driver, username, password):
    login_steps = LoginSteps(driver)
    login_steps.enter_credentials(username, password)


@when("I click login button")
def click_login(driver):
    login_steps = LoginSteps(driver)
    login_steps.click_login()


@then("the URL should contain \"dashboard\"")
def verify_dashboard_in_url(driver):
    login_steps = LoginSteps(driver)
    assert login_steps.verify_url_contains_dashboard() == True


@then(parsers.parse('I should see error message "{expected_message}"'))
def verify_error_message(driver, expected_message):
    login_steps = LoginSteps(driver)
    actual_message = login_steps.get_error_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"