import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class CheckoutPageLocators:
    titleCheckoutPage = (By.CSS_SELECTOR, "#content>h1")
    btnContinueBiDe = (By.ID, "button-payment-address")
    btnContinueDeDe = (By.ID, "button-shipping-address")
    btncontinueDeMe = (By.ID, "button-shipping-method")
    checkboxTermsConditions = (By.CSS_SELECTOR, "#collapse-payment-method input[type=checkbox]:nth-child(2)")
    btnContinuePaMe = (By.ID, "button-payment-method")
    btnConfirmOrder = (By.ID, "button-confirm")
    messageTransactionSuccess = (By.CSS_SELECTOR, "#content>p:nth-child(2)")
    textFieldComment = (By.CSS_SELECTOR, "#collapse-payment-method>div>p:nth-child(4)>textarea")
    titleTransactionSuccess = (By.CSS_SELECTOR, "#content>h1")
    btnContinueGiftConfirmation = (By.CSS_SELECTOR, "#content>div>div>a")


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver


    def showTitleAccountPage(self):
        return self.driver.find_element(*CheckoutPageLocators.titleCheckoutPage).text

    def selectBtnContinueCheckout(self):
        self.driver.find_element(*CheckoutPageLocators.btnContinueBiDe).click()
        self.driver.find_element(*CheckoutPageLocators.btnContinueDeDe).click()
        self.driver.find_element(*CheckoutPageLocators.btncontinueDeMe).click()
        self.driver.find_element(*CheckoutPageLocators.checkboxTermsConditions).click()
        self.driver.find_element(*CheckoutPageLocators.btnContinuePaMe).click()
        self.driver.find_element(*CheckoutPageLocators.btnConfirmOrder).click()

    def showSuccessMessageTransaction(self):
        return self.driver.find_element(*CheckoutPageLocators.messageTransactionSuccess).text

    def selectBtnContinueCheckoutGift(self, comment):
        self.driver.find_element(*CheckoutPageLocators.btnContinueBiDe).click()
        self.driver.find_element(*CheckoutPageLocators.textFieldComment).send_keys(comment)
        self.driver.find_element(*CheckoutPageLocators.checkboxTermsConditions).click()
        self.driver.find_element(*CheckoutPageLocators.btnContinuePaMe).click()
        self.driver.find_element(*CheckoutPageLocators.btnConfirmOrder).click()


    def showSuccessTitleTransaction(self):
        return self.driver.find_element(*CheckoutPageLocators.titleTransactionSuccess).text

    def selectBtnContinueGiftConfirmation(self):
        self.driver.find_element(*CheckoutPageLocators.btnContinueGiftConfirmation).click()


