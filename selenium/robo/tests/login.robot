*** Settings ***
Resource    ../resources/keywords/signup_keywords.robot

*** Test Cases ***
Verify User Can Login Successfully
    Open Demoblaze Application
    Click Login Menu
    Enter Login Username
    Enter Login Password
    Click Login Button
    Validate Successful Login
    Close Application

Verify Invalid User Login
    Open Demoblaze Application
    Click Login Menu
    Enter Invalid Login Username
    Enter Invalid Login Password
    Click Login Button
    Validate Invalid Login Alert
    Close Application