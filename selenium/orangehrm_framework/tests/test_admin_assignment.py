import pytest

from pages.login_page_assignment import LoginPage
from pages.admin_page_assignment import AdminPage


@pytest.mark.parametrize("username", [
    "Admin",
    "manda.user",
    "john.smith"
])
def test_user_exists(driver, username):

    login_page = LoginPage(driver)

    dashboard_page = login_page.login(
        "Admin",
        "admin123"
    )

    dashboard_page.side_menu.open_admin()

    admin_page = AdminPage(driver)

    result = admin_page.is_user_present(username)

    print(f"User Found Status: {result}")