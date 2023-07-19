from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.page = LoginPage(context.driver)
    context.page.load()


@when('I enter my username and password')
def step_impl(context):
    context.page.set_username(context.config.userdata['username'])
    context.page.set_password(context.config.userdata['password'])


@when('I click the login button')
def step_impl(context):
    context.page.click_login()


@then('I should be redirected to the home page')
def step_impl(context):
    assert str(context.page.get_title()).lower() == "test login | practice test automation"
