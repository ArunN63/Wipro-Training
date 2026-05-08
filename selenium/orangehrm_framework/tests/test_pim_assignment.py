from pages.login_page_assignment import LoginPage
from pages.pim_page_assignment import PIMPage



def test_view_employee_details(driver):

    login_page = LoginPage(driver)

    dashboard_page = login_page.login(
        "Admin",
        "admin123"
    )

    dashboard_page.side_menu.open_pim()

    pim_page = PIMPage(driver)

    personal_page = pim_page.view_employee_details("Linda")

    assert personal_page.is_personal_page_opened()