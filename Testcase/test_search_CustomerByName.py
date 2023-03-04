import time
from PageObject.loginpage1 import loginpage
from PageObject.AddCustomerpage import AddCustomer
from PageObject.SearchCustomerPage import findCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()  # Logger

    def test_searchCustomerByName(self, setup):
        self.logger.info("***Search Customer By Name_005***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***Login Successful***")

        self.logger.info("***Starting Search Customer By Name***")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmenu()
        self.addcust.clickoncustomersmenuitem()
        self.logger.info("***Search Customer By Name***")
        searchcust = findCustomer(self.driver)
        searchcust.setFirstName("Ashok")
        searchcust.setLastName("Kumar")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Ashok Kumar")
        assert True == status
        self.logger.info("***TC_SearchCustomerByEmail_004 Finished***")
        self.driver.close()