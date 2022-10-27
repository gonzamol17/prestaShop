import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class GiftCertificatePageLocators:
    titleGiftCertificate = (By.CSS_SELECTOR, "#content>p")
    recipientName = (By.ID, "input-to-name")
    recipientEmail = (By.ID, "input-to-email")
    yourNameField = (By.ID, "input-from-name")
    birthdayRadioButton = (By.CSS_SELECTOR, "#content div:nth-child(1) input[type=radio]")
    messageTextBox = (By.ID, "input-message")
    amountTextBox = (By.ID, "input-amount")
    checkboxAgree = (By.CSS_SELECTOR, "#content input[type=checkbox]:nth-child(1)")
    btnContinue = (By.CSS_SELECTOR, "#content input.btn.btn-primary")
    messageSuccess = (By.CSS_SELECTOR, "#content>p")
    btnContinue2 = (By.CSS_SELECTOR, "#content>div>div>a")
    btnCheckout = (By.CSS_SELECTOR, "#content div.pull-right>a")




class GiftCertificatePage:

    def __init__(self, driver):
        self.driver = driver


    def showTitleGiftCertificate(self):
        return self.driver.find_element(*GiftCertificatePageLocators.titleGiftCertificate).text

    def verifyTheCorrectUserName(self):
        return self.driver.find_element(*GiftCertificatePageLocators.yourNameField).get_attribute("value")

    def completeAllForm(self, name, email, message, amount):
        self.driver.find_element(*GiftCertificatePageLocators.recipientName).send_keys(name)
        self.driver.find_element(*GiftCertificatePageLocators.recipientEmail).send_keys(email)
        self.driver.find_element(*GiftCertificatePageLocators.birthdayRadioButton).click()
        self.driver.find_element(*GiftCertificatePageLocators.messageTextBox).send_keys(message)
        self.driver.find_element(*GiftCertificatePageLocators.amountTextBox).clear()
        self.driver.find_element(*GiftCertificatePageLocators.amountTextBox).send_keys(amount)
        self.driver.find_element(*GiftCertificatePageLocators.checkboxAgree).click()
        self.driver.find_element(*GiftCertificatePageLocators.btnContinue).click()


    def showTitleSuccessGiftCreated(self):
        return self.driver.find_element(*GiftCertificatePageLocators.messageSuccess).text

    def selectBtnContinueAndCheckout(self):
        self.driver.find_element(*GiftCertificatePageLocators.btnContinue2).click()
        self.driver.find_element(*GiftCertificatePageLocators.btnCheckout).click()
        time.sleep(2)





