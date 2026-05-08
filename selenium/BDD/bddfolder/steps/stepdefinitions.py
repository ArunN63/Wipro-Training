from re import search

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge import webdriver


@given(u'Buyer is on the OLX homepage')
def step_impl(context):
    context.driver=webdriver.Edge()
    context.driver.maximize_window()
    context.driver.get("https://www.olx.in/")

@when(u'buyer types product in search_input')
def step_impl(context):
    context.driver.find_element(By.ID,"searchbar")
    searchbar.send_keys("Cars")
    searchbar.send_keys(keys)
@then(u'search result should be displayed')
def step_impl(context):
    pass