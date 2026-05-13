from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
import time

scenarios('../features/employee_management.feature')

@given('I am logged in as "Admin" with password "admin123"')
def login_as_admin(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

@given('I navigate to the PIM module')
def navigate_to_pim(driver):
    dashboard = DashboardPage(driver)
    dashboard.navigate_to_pim()

@when('I click on the "Add Employee" button')
def click_add_employee(driver):
    pim_page = PIMPage(driver)
    pim_page.click_add_employee()

@when(parsers.parse('I enter first name "{first_name}" and last name "{last_name}"'))
def enter_employee_details(driver, first_name, last_name):
    pim_page = PIMPage(driver)
    pim_page.add_employee(first_name, last_name)

@when('I save the employee details')
def save_employee(driver):
    # Already saved in add_employee method
    time.sleep(2)

@then('I should see a success message "Successfully Saved"')
def verify_success_message(driver):
    pim_page = PIMPage(driver)
    message = pim_page.get_success_message()
    assert "Success" in message or "Successfully" in message, f"Expected success message, got {message}"

@then(parsers.parse('the employee "{full_name}" should be in the employee list'))
def verify_employee_in_list(driver, full_name):
    pim_page = PIMPage(driver)
    first_name, last_name = full_name.split()
    pim_page.search_employee(full_name)
    assert pim_page.is_employee_in_list(first_name, last_name), f"Employee {full_name} not found in list"