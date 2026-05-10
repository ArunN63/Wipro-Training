@Smoke
@Regression
@Profile

Feature: Profile Update

  Scenario: Update nickname and upload profile photo

    Given user logs into OrangeHRM
    When user navigates to My Info page
    And user updates nickname as "Sindhu"
    And user uploads profile image
    Then profile should update successfully