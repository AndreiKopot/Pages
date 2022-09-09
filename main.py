from selenium import webdriver
from Form_Authentication import FormAuth
from Logout_page import LogOut
from HomeView import HomeView

driver = webdriver.Chrome()
try:
    home = HomeView(driver)
    home.nav_to_login()
    
    form_auth = FormAuth(driver)
    form_auth.insert_username('tomsmith')
    form_auth.insert_password('SuperSecretPassword!')
    form_auth.click_button()

    log_out = LogOut(driver)
    log_out.click_logout()
    assert 'logged out' in log_out.flash_text()
        
finally:
   driver.quit()