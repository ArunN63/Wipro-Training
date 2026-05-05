import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
#driver.get("https://www.google.com")

#ID
# search_input=driver.find_element(By.ID,"APjFqb")
# search_input.send_keys("selenium")
# time.sleep(3)
# search_input.clear()
# time.sleep(2)


# search_input=driver.find_element(By.NAME,"q")
# search_input.send_keys("locators")
# time.sleep(3)

#Name
# googlesearch_button=driver.find_element(By.NAME,"btnK")
# googlesearch_button.click()
# time.sleep(10)

#Classname
# infl_button=driver.find_element(By.NAME,"RNmpXc")
# infl_button.click()
# time.sleep(10)

#Tagnane
# href_elements=driver.find_elements(By.TAG_NAME,"a")
# for elnt in href_elements:
#     print(f"{elnt.text}-{elnt.get_attribute('href')}")

#link text
# images_link=driver.find_element(By.LINK_TEXT,"Images")
# images_link.click()
# time.sleep(10)

#Partial Link Test
# images_link=driver.find_element(By.PARTIAL_LINK_TEXT,"Ima")
# images_link.click()
# time.sleep(10)

#CSS selector
# search_input=driver.find_element(By.CSS_SELECTOR,"div>textarea")
# search_input.send_keys("selenium")
# time.sleep(10)

#Xpath
# settings_text=driver.find_elements(By.XPATH,'/html/body/div[7]/div/div[2]/div[2]/span/span/g-popup/div[1]/div')
# print(settings_text.text)
# time.sleep(5)


#AND and OR Expressions
# driver.get("https://the-internet.herokuapp.com/tables")
# time.sleep(5)
# and_example=driver.find_element(By.XPATH,"//td[text()='Tim' and @class='first-name']")
# print(f"AND Example found on both conditions:{and_example.text}")

# or_example = driver.find_element(By.XPATH, "//td[text()='Tim' or text()='Frank']")
# print(f"or Example found on both conditions:{or_example.text}")

#CHILD-SELECT all 'td' elements that are direct children of  a row
# rows=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td")
# print(f"child example found{len(rows)}coloums in the first table")

#parent-get the parent row of  a particular cell
# email_cell = driver.find_element(By.XPATH, "//td[text()='jdoe@hotmail.com']")
# parent_row = driver.find_element(By.XPATH, "//td[text()='jdoe@hotmail.com']/parent::tr")
# print(parent_row.find_element(By.XPATH, "./td[2]").text)
#Ancestor-get the table element that is an ancestor of  a cell
# ancestor_table = driver.find_element(By.XPATH, "//td[text()='jsmith@gmail.com']/ancestor::table")
# print(ancestor_table.get_attribute('id'))

#Descendant-find all descendants(cells)under the table
# descendants = driver.find_elements(By.XPATH, "//table[@id='table1']//td")
# print(len(descendants))

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
# locate elements
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
# enter credentials
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
time.sleep(1)
# click login
login_button.click()
time.sleep(3)
# reference element (Twitter)
twitter_icon = driver.find_element(By.LINK_TEXT, "Twitter")
# to_right_of → Facebook
facebook_icon = driver.find_element(
    locate_with(By.TAG_NAME, "a").to_right_of(twitter_icon)
)
print("toRightOf Example →", facebook_icon.get_attribute("href"))
# to_left_of → Twitter (from Facebook)
left_icon = driver.find_element(
    locate_with(By.TAG_NAME, "a").to_left_of(facebook_icon)
)
print("toLeftOf Example →", left_icon.get_attribute("href"))
# near → closest element to Facebook
near_element = driver.find_element(
    locate_with(By.TAG_NAME, "a").near(facebook_icon)
)
print("Near Example →", near_element.get_attribute("href"))
time.sleep(3)
# close browser
driver.quit()