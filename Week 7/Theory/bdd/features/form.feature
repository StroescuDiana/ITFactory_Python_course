Feature: Login

Scenario: Login Successfully
  Given I am on the login page
  When I enter my username and password
  And I click the login button
  Then I should be redirected to the successfully login page
