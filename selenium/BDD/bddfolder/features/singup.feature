Feature: Signup Functionality

  Background:
    Given User launches Demoblaze application

#  @smoke @signup
  Scenario: Successful Signup
    When User clicks on Sign up menu
    And User enters signup username "edfrgthyjudfgvbhnjdfvgbnhj"
    And User enters signup password "ojrgebrgehbgbrhgbrhbrg"
    And User clicks Signup button
    Then User should see signup success message

#  @negative @signup
#  Scenario Outline: Signup with existing username
#    When User clicks on Sign up menu
#    And User enters signup username "<username>"
#    And User enters signup password "<password>"
#    And User clicks Signup button
#    Then User should see signup error message
#
#    Examples:
#      | username | password |
#      | testuser | test123  |
#      | admin    | admin123 |
#
#  @negative @signup
#  Scenario Outline: Signup with empty fields
#    When User clicks on Sign up menu
#    And User enters signup username "<username>"
#    And User enters signup password "<password>"
#    And User clicks Signup button
#    Then User should see signup validation alert
#
#    Examples:
#      | username | password |
#      |          | test123  |
#      | user123  |          |
#      |          |          |