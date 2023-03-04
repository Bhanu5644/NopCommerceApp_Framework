from selenium.webdriver.common.by import By
from PageObject.loginpage1 import loginpage
from PageObject.AddCustomerpage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random


class Test003Addcustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()  # Logger

    def addcustomer(self, setup):
        self.logger.info("***Test_003_AddCustomer***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("***Login Successful***")

        self.logger.info("***Starting Add Customer Test***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmenu()
        self.addcust.clickoncustomersmenuitem()

        self.addcust.clickonaddnew()

        self.logger.info("***Providing Customer Information***")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setcustomerroles("Guests")
        self.addcust.setmanagerofvendor("Vendor2")
        self.addcust.setgender("Male")
        self.addcust.setfirstname("munish")
        self.addcust.setlastname("sandhu")
        self.addcust.setdob("18/12/1986")
        self.addcust.setcompanyname("Huawei")
        self.addcust.setadmincontent("This is for Testing...")
        self.addcust.clickonsave()

        self.logger.info("***Saving Customer info***")

        self.logger.info("***Add Customer Validation Started***")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***Add Customer Test Passed***")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_customer_scr.png")  # Screenshot
            self.logger.info("***Add Customer Test Failed***")
            assert True == False

        self.driver.close()
        self.logger.info("****Ending Home page Title***")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))