from selenium.webdriver.common.by import By

from Base_page import BaseView 

class LogOut(BaseView):
    LOG_OUT_BUTTON = (By.LINK_TEXT, 'Logout')
    FLASH_TEXT = (By.CSS_SELECTOR, '#flash')

    
    def click_logout(self):

        self.wait_for(self.LOG_OUT_BUTTON).click()
 

    def flash_text(self):

        return self.wait_for(self.FLASH_TEXT).text

   