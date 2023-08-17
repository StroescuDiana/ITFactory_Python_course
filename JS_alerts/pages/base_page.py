from utils.browser import Browser


class Base_page(Browser):

    def navigate_to_alerts_page(self):
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')
