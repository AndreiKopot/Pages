
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from Base_page import BaseView

class HomeView(BaseView):
    site_url = 'https://the-internet.herokuapp.com/'
    FORM_AUTH = (By.LINK_TEXT, 'Form Authentication')

    
    def nav_to_login(self):
        self.driver.get(self.site_url)

        self.wait_for(self.FORM_AUTH).click()
