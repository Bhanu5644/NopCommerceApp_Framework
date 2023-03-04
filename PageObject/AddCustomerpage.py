import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    # Add Customer Detail
    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@name='Email']"
    txtPassword_xpath = "//input[@name='Password']"
    lstitemAdminstrations_xpath = "//span[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//span[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//span[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//span[contains(text(),'Vendors')]"
    drpmgrOfVender_xpath = "//*[@ID='VendorId']"
    rdMalegender_id = "Gender_Male"
    rdFemalegender_id = "Gender_Female"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtComapnyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//*[@id='AdminComment']"
    btnSave_xpath = "//*[@name='save']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"

    def __init__(self, driver):
        self.driver = driver

    def clickoncustomersmenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickoncustomersmenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickonaddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(password)

    def setcustomerroles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Adminstrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdminstrations_xpath)
        elif role == 'Guests':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click();  Because this is not working so using JavaScript#
        self.driver.execute_script("arguments[0].click();", self.listitem)    # Java script  Statement

    def setmanagerofvendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVender_xpath))
        drp.select_by_visible_text(value)

    def setgender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMalegender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemalegender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMalegender_id).click()

    def setfirstname(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstname_xpath).send_keys(fname)

    def setlastname(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastname_xpath).send_keys(lname)

    def setdob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setcompanyname(self, comname):
        self.driver.find_element(By.XPATH, self.txtComapnyName_xpath).send_keys(comname)

    def setadmincontent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickonsave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()