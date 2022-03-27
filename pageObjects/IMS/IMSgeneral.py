from selenium import webdriver
from selenium.webdriver.common.by import By

class IMSloginc:
    textbox_adminemailaddress_css = "input[name=email]"
    textbox_adminpassword_xpath = "//*[@id='password']"
    button_login_XPATH = "//*[@id='call-for-entry']/div/main/div/form/button/span[1]"
    button_IMSlogout_XPATH = "//*[@id='call-for-entry']/div[1]/header/div/div/i"

    def __init__(self,driver):
        self.driver = driver

    def enterAdminEmailAddress(self,adminemailaddress):
        self.driver.find_element(By.CSS_SELECTOR,self.textbox_adminemailaddress_css).click()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_adminemailaddress_css).send_keys(adminemailaddress)

    def enterAdminPassword(self,adminPassword):
        self.driver.find_element(By.XPATH,self.textbox_adminpassword_xpath).click()
        self.driver.find_element(By.XPATH,self.textbox_adminpassword_xpath).send_keys(adminPassword)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_XPATH).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.button_IMSlogout_XPATH).click()




