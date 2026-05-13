@Profile
Feature: Profile Update

  Background: Employee is logged in
    Given I open OrangeHRM login page
    And I enter username "Admin" and password "admin123"
    And I click login button
    And I navigate to My Info section

  @Smoke
  Scenario: Update nickname and upload profile photo
    When I click on Personal Details
    And I change my nickname to "Johnny"
    And I upload profile photograph "download.jpg"
    And I click Save button
    Then I should see success message "Successfully Updated"
    And my nickname should be displayed as "Johnny"