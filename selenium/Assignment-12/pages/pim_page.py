from selenium.webdriver.common.by import By


class PimPage:

    pim_menu = (By.XPATH, "//span[text()='PIM']")
    add_employee = (By.XPATH, "//a[contains(text(),'Add Employee')]")

    firstname = (By.NAME, "firstName")
    lastname = (By.NAME, "lastName")

    save_btn = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):

        self.driver = driver

    def click_pim(self):

        self.driver.find_element(*self.pim_menu).click()

    def click_add_employee(self):

        self.driver.find_element(*self.add_employee).click()

    def enter_firstname(self, fname):

        self.driver.find_element(*self.firstname).send_keys(fname)

    def enter_lastname(self, lname):

        self.driver.find_element(*self.lastname).send_keys(lname)

    def click_save(self):

        self.driver.find_element(*self.save_btn).click()