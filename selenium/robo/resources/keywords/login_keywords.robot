*** Settings ***
Library     SeleniumLibrary
Library     ../pages/login_page.py

*** Keywords ***
Open Demoblaze Application
    Launch Demoblaze Application

Click Login Menu
    Click Login Link

Enter Login Username
    Enter Username

Enter Login Password
    Enter Password

Click Login Button
    Click Signin Button

Validate Successful Login
    Verify Successful Login

Close Application
    Close Browser

Enter Invalid Login Username
    Enter Invalid Login Username

Enter Invalid Login Password
    Enter Invalid Login Password

Validate Invalid Login Alert
    Validate Invalid Login Alert