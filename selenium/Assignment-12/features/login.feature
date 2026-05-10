Feature: User Authentication

  Background:
    Given user launches OrangeHRM login page

  Scenario: Successful login with valid credentials
    When user enters username "Admin"
    And user enters password "admin123"
    And user clicks login button
    Then user should navigate to dashboard

  Scenario: Unsuccessful login with invalid password
    When user enters username "Admin"
    And user enters password "wrong123"
    And user clicks login button
    Then invalid credentials message should display