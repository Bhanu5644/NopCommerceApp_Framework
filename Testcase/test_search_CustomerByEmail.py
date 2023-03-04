import time
from PageObject.loginpage1 import loginpage
from PageObject.AddCustomerpage import AddCustomer
from PageObject.SearchCustomerPage import findCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()  # Logger

    def test_searchCustomerByemail(self, setup):
        self.logger.info("***Search Customer By Email_004***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***Login Successful***")

        self.logger.info("***Starting Search Customer By Email***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmenu()
        self.addcust.clickoncustomersmenuitem()
        self.logger.info("***Search Customer By EmailID***")
        searchCust = findCustomer(self.driver)
        searchCust.setEmail("victoria_victoria@nopCommerce.com")
        searchCust.clickSearch()
        time.sleep(5)
        status = searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("***TC_SearchCustomerByEmail_004 Finished***")
        self.driver.close()