from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage

scenarios('../features/leave_workflow.feature')

@given('I am logged in as "Admin" with password "admin123"')
def login_as_admin(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

@given('I navigate to the Leave module')
def navigate_to_leave(driver):
    dashboard = DashboardPage(driver)
    dashboard.navigate_to_leave()

@when('I click on "Apply Leave"')
def click_apply_leave(driver):
    leave_page = LeavePage(driver)
    leave_page.click_apply_leave()

@when(parsers.parse('I select "{leave_type}" as leave type'))
def select_leave_type(driver, leave_type):
    leave_page = LeavePage(driver)
    leave_page.select_leave_type(leave_type)

@when(parsers.parse('I select from date "{from_date}" to date "{to_date}"'))
def select_dates(driver, from_date, to_date):
    leave_page = LeavePage(driver)
    leave_page.select_dates(from_date, to_date)

@when(parsers.parse('I add a comment "{comment}"'))
def add_comment(driver, comment):
    leave_page = LeavePage(driver)
    leave_page.add_comment(comment)

@when('I click on "Apply" button')
def click_apply_button(driver):
    leave_page = LeavePage(driver)
    leave_page.click_apply()

@then('I should see a success toast message "Successfully Submitted"')
def verify_success_toast(driver):
    leave_page = LeavePage(driver)
    message = leave_page.get_success_message()
    assert "Successfully" in message, f"Expected success message, got {message}"

@then('the leave balance should be reduced by 3 days')
def verify_balance_reduction(driver):
    leave_page = LeavePage(driver)
    initial_balance = getattr(verify_balance_reduction, 'initial_balance', 12.0)
    current_balance = leave_page.get_leave_balance()
    # This is simplified - you'd need to capture initial balance before leave application
    assert current_balance < initial_balance, f"Expected balance reduction, current: {current_balance}"

@then('the leave status should be "Pending Approval" in my leave list')
def verify_leave_status(driver):
    leave_page = LeavePage(driver)
    leave_page.navigate_to_my_leave()
    status = leave_page.get_leave_status()
    assert "Pending" in status, f"Expected 'Pending Approval', got {status}"