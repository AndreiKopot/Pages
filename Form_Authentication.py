from selenium.webdriver.common.by import By

from Base_page import BaseView 

class FormAuth(BaseView):
  
    USERNAME = (By.CSS_SELECTOR, '#username')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type=submit]')


    
    def insert_username(self, username):

        self.wait_for(self.USERNAME).send_keys(username)
        
    def insert_password(self, password):
        self.find(self.PASSWORD).send_keys(password)

    def click_button(self):
        self.find(self.LOGIN_BUTTON).click()