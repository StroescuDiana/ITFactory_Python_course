Feature: Unit test exercises

Background:
   Given the unit tests are initialized

@given
Scenario: Test given
  Given "a scenario is initialized"

@when
Scenario: Test when
  When "an action is performed"

@then
Scenario: Test then
  Then "an outcome is verified"

Scenario Outline: Test parameters
  Given "<step>"
  When "<action>"
  Then "<outcome>"

Examples:
  | step | action | outcome |
  | "a scenario is initialized" | "an action is performed" | "an outcome is verified" |

@smoke
Scenario: Test tag
   Given "a scenario is running"