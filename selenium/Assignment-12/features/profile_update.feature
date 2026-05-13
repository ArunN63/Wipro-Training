@Profile
Feature: Profile Update
  As an employee
  I want to update my personal information
  So that my profile remains accurate

  Background: Employee is logged into the system
    Given I am logged in as "Admin" with password "admin123"
    And I navigate to "My Info" section

  @Smoke @Profile @Regression
  Scenario: Update nick name and upload profile photo
    When I click on "Personal Details"
    And I change my nickname to "Johnny"
    And I upload a profile photograph "profile_pic.jpg"
    And I click on "Save" button
    Then I should see a success message "Successfully Updated"
    And my nickname should be displayed as "Johnny"
    And my profile picture should be visible

  @Regression @Profile
  Scenario: Update contact details
    When I click on "Contact Details"
    And I update my mobile number to "9876543210"
    And I save the changes
    Then I should see a success message