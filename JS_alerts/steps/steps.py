from behave import *


@given('I am on the JavaScript Alerts homepage')
def step_impl(context):
    context.basepage.navigate_to_alerts_page()
    print(u'STEP: Given I am on the JavaScript Alerts homepage')


@when('I click on JS Alert button')
def step_impl(context):
    context.alerts.click_JS_alert_button()
    print(u'STEP: When I click on JS Alert button')


@when('I accept JS Alert')
def step_impl(context):
    context.alerts.accept_alert()
    print(u'STEP: When I accept JS Alert')


@then('I get a result message for JS Alert')
def step_impl(context):
    context.alerts.message_alert()
    print(u'STEP: Then I get a result message for JS Alert')


@when('I click on JS Confirm button')
def step_impl(context):
    context.alerts.click_JS_Confirm_button()
    print(u'STEP: When I click on JS Confirm button')


@when('I dismiss JS COnfirm alert')
def step_impl(context):
    context.alerts.dismiss_alert()
    print(u'STEP: When I dismiss JS COnfirm alert')


@then('I get result message for JS Confirm')
def step_impl(context):
    context.alerts.message_confirm()
    print(u'STEP: Then I get result message for JS Confirm')


@when('I click on JS Prompt button')
def step_impl(context):
    context.alerts.click_JS_Prompt_button()
    print(u'STEP: When I click on JS Prompt button')


@when('I send some text')
def step_impl(context):
    context.alerts.send_text()
    print(u'STEP: When I send some text')


@when(u'I accept JS Prompt alert')
def step_impl(context):
    context.alerts.accept_Js_Prompt()
    print(u'STEP: When I accept JS Prompt alert')


@then('I get result message for JS Prompt')
def step_impl(context):
    context.alerts.message_prompt()
    print(u'STEP: Then I get result message for JS Prompt')


@given('I am on the login page')
def step_impl(context):
    print(u'STEP: Given I am on the login page')


@when('I introduce a valid username')
def step_impl(context):
    print(u'STEP: When I introduce a valid username')


@when('I introduce a valid password')
def step_impl(context):
    print(u'STEP: When I introduce a valid password')


@when('I click on login button')
def step_impl(context):
    print(u'STEP: When I click on login button')


@then('I get a succes message login')
def step_impl(context):
    print(u'STEP: Then I get a succes message login')


@then('I get an unsuccessful message')
def step_impl(context):
    print(u'STEP: Then I get an unsuccessful message')


@when('I introduce an invalid "{username}" or "{password}"')
def step_impl(context, username, password):
    print(u'STEP: When I introduce an invalid "{username}" or "{password}"')
