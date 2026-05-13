Feature: Employee Management

  Background: Admin is logged in
    Given I open OrangeHRM login page
    And I enter username "Admin" and password "admin123"
    And I click login button
    And I navigate to PIM module

  @Smoke
  Scenario Outline: Add multiple new employees
    When I click on Add Employee button
    And I enter "<FirstName>" and "<LastName>"
    And I click Save button
    Then I should see success message "Successfully Saved"

    Examples:
      | FirstName | LastName   |
      | John      | Wick       |
      | Sarah     | Johnson    |
      | Michael   | Chen       |