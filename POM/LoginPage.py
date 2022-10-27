import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class LoginPageLocators:
    titleLoginPage = (By.CSS_SELECTOR, "#main>header>h1")
    linkCreateNewAccount = (By.CSS_SELECTOR, "#content>div>a")
    txtEmailBox = (By.ID, "input-email")
    txtPasswordBox = (By.ID, "input-password")
    btnLogin = (By.CSS_SELECTOR, "#content div>form>input")



class LoginPage:

    def __init__(self, driver):
        self.driver = driver


    def showTitleLoginPage(self):
        return self.driver.find_element(*LoginPageLocators.titleLoginPage).text

    def selectLinkCreateNewAccount(self):
        self.driver.find_element(*LoginPageLocators.linkCreateNewAccount).click()

    def tryLoginUser(self, email, password):
        self.driver.find_element(*LoginPageLocators.txtEmailBox).send_keys(email)
        self.driver.find_element(*LoginPageLocators.txtPasswordBox).send_keys(password)
        self.driver.find_element(*LoginPageLocators.btnLogin).click()


