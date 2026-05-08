import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest_check as check

@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle=driver.title
    assert pagetitle=='Google','Google Home Page Not Loaded'

def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT, 'Images').click()
    pagetitle = driver.title
    assert 'Google Images' in pagetitle, 'Images Page Not Loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT,'Business').click()
    time.sleep(1)
    # assert 'Business' in driver.title, 'Business Page Not Loaded-Title check'
    # assert 'business' in driver.current_url,'Business Page Not Loaded-URL check'
    check.equal(driver.title, 'Business','Business Page Not Loaded-Title check')
    check.is_in("business",driver.current_url,"Business Page Not Loaded-URL check")