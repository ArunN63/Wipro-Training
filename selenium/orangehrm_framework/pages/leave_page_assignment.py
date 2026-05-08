from pages.side_menu_component_assignment import SideMenuComponent


class LeavePage:

    def __init__(self, driver):
        self.driver = driver
        self.side_menu = SideMenuComponent(driver)