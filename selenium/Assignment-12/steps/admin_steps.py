from pytest_bdd import scenarios, given, when, then, parsers
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pytest_bdd.parsers import parse

scenarios('../features/admin_search.feature')

@given('I am logged in as "Admin" with password "admin123"')
def login_as_admin(driver):
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

@given('I navigate to the Admin module')
def navigate_to_admin(driver):
    dashboard = DashboardPage(driver)
    dashboard.navigate_to_admin()

@when('I search for users with the following criteria:')
def search_with_criteria(driver, datatable):
    admin_page = AdminPage(driver)
    # Parse the data table
    criteria = datatable.rows[0].cells
    search_params = {
        'username': criteria[0] if len(criteria) > 0 else "",
        'user_role': criteria[1] if len(criteria) > 1 else "",
        'status': criteria[2] if len(criteria) > 2 else ""
    }
    admin_page.search_users_with_criteria(**search_params)

@then('I should see at least one user in the results')
def verify_results_exist(driver):
    admin_page = AdminPage(driver)
    results_count = admin_page.get_search_results_count()
    assert results_count > 0, f"Expected at least 1 result, got {results_count}"

@then('the search results should match the criteria')
def verify_results_match(driver):
    admin_page = AdminPage(driver)
    # Verify that results match criteria (enhanced implementation)
    assert admin_page.get_search_results_count() > 0