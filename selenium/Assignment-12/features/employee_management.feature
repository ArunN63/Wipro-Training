Feature: Employee Management (PIM)
  As an HR admin
  I want to add new employees
  So that I can maintain the employee database

  Background: Admin is logged into the system
    Given I am logged in as "Admin" with password "admin123"
    And I navigate to the PIM module

  @Smoke @Regression @PIM
  Scenario Outline: Add multiple new employees
    When I click on the "Add Employee" button
    And I enter first name "<FirstName>" and last name "<LastName>"
    And I save the employee details
    Then I should see a success message "Successfully Saved"
    And the employee "<FirstName> <LastName>" should be in the employee list

    Examples:
      | FirstName | LastName   |
      | John      | Wick       |
      | Sarah     | Johnson    |
      | Michael   | Chen       |
      | Emma      | Rodriguez  |
      | William   | Turner     |