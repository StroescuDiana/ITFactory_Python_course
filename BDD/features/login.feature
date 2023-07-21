Feature: Login
  Scenario: Successful Login
    Given I am on the login page
    When I enter my username and password
    And I click on Submit button
    Then I should be redirected on home page