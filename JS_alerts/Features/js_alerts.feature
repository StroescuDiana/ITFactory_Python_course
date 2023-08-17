Feature: Test JavaScripts Alerts

  Background:
    Given I am on the JavaScript Alerts homepage

  @JS_alert
  Scenario: Check JS Alert
    When I click on JS Alert button
    And I accept JS Alert
    Then I get a result message for JS Alert

  @JS_confirm
  Scenario: Check JS Confirm
    When I click on JS Confirm button
    And I dismiss JS COnfirm alert
    Then I get result message for JS Confirm

  @JS_prompt
  Scenario: Check JS Prompt
    When I click on JS Prompt button
    And I send some text
    And I accept JS Prompt alert
    Then I get result message for JS Prompt

