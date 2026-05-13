Feature: Leave Application Workflow

  Background: Employee is logged in
    Given I open OrangeHRM login page
    And I enter username "Admin" and password "admin123"
    And I click login button
    And I navigate to Leave module

  Scenario: Apply for Medical Leave
    When I click on Apply Leave
    And I select "Medical Leave" as leave type
    And I select from date "2026-05-20" to date "2026-05-20"
    And I click Apply button
    Then I should see success toast message "Successfully Submitted"
    And my leave balance should be reduced by 1 day