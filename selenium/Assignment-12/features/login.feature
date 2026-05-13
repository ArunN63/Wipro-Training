Feature: User Authentication
  As an employee
  I want to login to OrangeHRM
  So that I can access my dashboard

  Background: User is on login page
    Given I am on the OrangeHRM login page

  @Smoke @Critical
  Scenario: Successful login with valid credentials
    When I enter username "Admin" and password "admin123"
    And I click on the login button
    Then I should be redirected to the dashboard page
    And I should see "Dashboard" in the page title

  @Regression @Negative
  Scenario: Unsuccessful login with invalid password
    When I enter username "Admin" and password "wrongpassword123"
    And I click on the login button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page