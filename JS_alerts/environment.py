from utils.browser import Browser
from pages.alerts_page import Alerts
from pages.base_page import Base_page


def before_all(context):
    context.browser = Browser()
    context.alerts = Alerts()
    context.basepage = Base_page()

def after_all(context):
    context.browser.close()