from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager



browser=input('what browser do you want to use')
match (browser.lower()):
    case 'chrome':
        driver=webdriver.Chrome(service=Service('../resources/msedgedriver.exe'))
    case 'edge':
        driver=webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
    case _:
        print('unknow browser-not avaliable.\n Executing with deafault EDGE browser.')
        driver=webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https://www.google.com")

sleep(3)

pagetitle=driver.title
if pagetitle=='Google':
    print("google homepage loaded-pass")
else:
    print("google homepage not loaded-fail")
driver.quit()
