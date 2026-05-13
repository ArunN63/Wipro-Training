Feature: User Authentication

  Background: User is on login page
    Given I open OrangeHRM login page

  @Smoke
  Scenario: Successful login with valid credentials
    When I enter username "Admin" and password "admin123"
    And I click login button
    Then the URL should contain "dashboard"