class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_XPATH = "//button[@type='submit']"
    link_logout_LINKTEXT = "logout"

    def __int__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).sendkey("username")

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).sendkey("password")

    def clicklogin(self):
        self.driver.find_element_by_XPATH(self.button_login_XPATH).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_LINKTEXT).click()

