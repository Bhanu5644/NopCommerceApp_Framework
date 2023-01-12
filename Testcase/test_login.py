import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage

class test_001_Login:
    baseURL="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password = "admin"

    def __init__(self):
        self.driver = None

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False



