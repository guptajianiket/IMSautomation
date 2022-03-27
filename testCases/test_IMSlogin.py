from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from pageObjects.IMS.IMSgeneral import IMSloginc


class Test_001_Login:
    baseURL = "https://interactivity-staging-viacom18.web.app/landing"
    adminemail = "vaibhav.sharma@webdunia.net"
    adminpasswd = "Admin@Viacom18"
    service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    def test_IMSpageload(self):
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Voot - Interactivity CMS":
            assert True
        else:
            assert False

    def test_IMSpagelogin(self):
        self.driver.maximize_window()
        self.imslp = IMSloginc(self.driver)
        self.imslp.enterAdminEmailAddress(self.adminemail)
        time.sleep(2)
        self.imslp.enterAdminPassword(self.adminpasswd)
        self.imslp.clickLogin()
        act_title = self.driver.title
        if act_title == "Voot - Interactivity CMS":
            assert True
        else:
            assert False

    