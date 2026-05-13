Feature: Leave Application Workflow
  As an employee
  I want to apply for medical leave
  So that I can request time off for health reasons

  Background: Employee is logged into the system
    Given I am logged in as "Admin" with password "admin123"
    And I navigate to the Leave module

  @Regression @Leave
  Scenario: Apply for Medical Leave and verify status
    When I click on "Apply Leave"
    And I select "Medical Leave" as leave type
    And I select from date "2026-05-20" to date "2026-05-22"
    And I add a comment "Medical appointment"
    And I click on "Apply" button
    Then I should see a success toast message "Successfully Submitted"
    And the leave balance should be reduced by 3 days
    And the leave status should be "Pending Approval" in my leave list