import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AccountPageLocators:
    titleAccountPage = (By.CSS_SELECTOR, "#content>h2:nth-child(1)")
    newsLetterLink = (By.CSS_SELECTOR, "#content>ul:nth-child(8) a")
    radioButtonYes = (By.CSS_SELECTOR, "input[type='radio'][value='1']")
    radioButtonNo = (By.CSS_SELECTOR, "input[type='radio'][value='0']")
    btnContinue = (By.CSS_SELECTOR, "#content div.pull-right>input")
    unsuscribeMessageNewsLetter = (By.CSS_SELECTOR, "#account-account>div.alert.alert-success.alert-dismissible")
    affiliateAccountLink = (By.CSS_SELECTOR, "#content>ul:nth-child(6)>li>a")


class AccountPage:

    def __init__(self, driver):
        self.driver = driver


    def showTitleAccountPage(self):
        return self.driver.find_element(*AccountPageLocators.titleAccountPage).text

    def selectNewsLetterLink(self):
        self.driver.find_element(*AccountPageLocators.newsLetterLink).click()

    def showRadioButtonYesStatus(self):
        return self.driver.find_element(*AccountPageLocators.radioButtonYes).is_selected()

    def selectNoSubscriptionOnNewsLetter(self):
        self.driver.find_element(*AccountPageLocators.radioButtonNo).click()

    def selectContinueBtn(self):
        self.driver.find_element(*AccountPageLocators.btnContinue).click()

    def showSuccessUnsuscribeNewsLetter(self):
        return self.driver.find_element(*AccountPageLocators.unsuscribeMessageNewsLetter).text

    def selectAffiliateAccount(self):
        self.driver.find_element(*AccountPageLocators.affiliateAccountLink).click()

