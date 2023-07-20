from behave import *


@given('the unit tests are initialized')
def setup(context):
    pass


@given('"a scenario is initialized"')
def given_step(context):
    pass


@when('I click the login button')
def when_step(context):
    pass


@then('"an outcome is verified"')
def then_step(context):
    pass


@given("<step>")
def scenario_outline_step(context, step):
    pass
