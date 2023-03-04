import pytest

from PageObject.loginpage1 import loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger=LogGen.loggen()
    @pytest.mark.sanity

    def test_homepage_title(self,setup):
        self.logger.info("***Test_001_Login***")
        self.logger.info("***Verifying Home Page Title***")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***Home Page Title is passed***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage.png")
            self.driver.close()
            self.logger.error("***Home Page Title is Failed*****")
            assert False

    def test_login(self,setup):
        self.logger.info("***Verifying Login Test***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("***Login Test is passed***")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("***Login Test is Failed***")
            assert False


