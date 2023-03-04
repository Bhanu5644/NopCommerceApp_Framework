from selenium.webdriver.common.by import By

class loginpage:
    textbox_username_XPATH = "//*[@id='Email']"
    textbox_password_id = "Password"
    button_login_XPATH = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_XPATH).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_XPATH).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_XPATH).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()