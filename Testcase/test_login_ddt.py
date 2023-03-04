import time
from PageObject.loginpage1 import loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".\\TestData\\Logindata.xlsx"
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("***Test_002_DDT_Login***")
        self.logger.info("***Verifying Login DDT Test***")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=loginpage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("number of Rows in excel:",self.rows)

        lst_status=[]  # Empty list variable

        for r in range(2,self.rows+1):
            self.user=XLUtils.readDatal(self.path,'Sheet1',r,1)
            self.Password = XLUtils.readDatal(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readDatal(self.path,'Sheet1',r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.Password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("****Passes***")
                    self.lp.clicklogout();
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("****Failed***")
                    self.lp.clicklogout();
                    lst_status.append("Fail")
            elif act_title !=exp_title:
                if self.exp=="Pass":
                    self.logger.info("****Failed***")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("****Passed***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("***Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("**** End of login DDT Test****")
        self.logger.info("**** Completed TC_login DDT_002*****");