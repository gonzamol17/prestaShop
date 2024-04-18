import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AffiliateAccountLocators:
    btn_Continue = (By.CSS_SELECTOR, "#content input.btn.btn-primary")
    error_AboutUs = (By.CSS_SELECTOR, "#account-affiliate>div.alert.alert-danger.alert-dismissible")
    checkboxAboutUs = (By.CSS_SELECTOR, "#content input[type=checkbox]:nth-child(2)")
    error_ChequePaye = (By.CSS_SELECTOR, "#payment-cheque>div>div")
    companyField = (By.ID, "input-company")
    websiteField = (By.ID, "input-website")
    taxIdField = (By.ID, "input-tax")
    chequePayeNameField = (By.ID, "input-cheque")
    paypelEmailAccountField = (By.ID, "input-paypal")
    bankNameField = (By.ID, "input-bank-name")
    branchNumberField = (By.ID, "input-bank-branch-number")
    swiftCodeField = (By.ID, "input-bank-swift-code")
    accountNameField = (By.ID, "input-bank-account-name")
    accountNumberField = (By.ID, "input-bank-account-number")


class AffiliateAccountPage:

    def __init__(self, driver):
        self.driver = driver


    def selectBtnContinue(self):
        return self.driver.find_element(*AffiliateAccountLocators.btn_Continue).click()

    def showErrorAboutUs(self):
        return self.driver.find_element(*AffiliateAccountLocators.error_AboutUs).text

    def selectAboutUs(self):
        self.driver.find_element(*AffiliateAccountLocators.checkboxAboutUs).click()

    def showErrorChequePaye(self):
        return self.driver.find_element(*AffiliateAccountLocators.error_ChequePaye).text

    def showColorOfErrorChequePaye(self):
        return self.driver.find_element(*AffiliateAccountLocators.error_ChequePaye)

    def selectPaymentMethodOption(self, option):
        self.driver.find_element(By.CSS_SELECTOR, "#content input[value="+option+"]").click()
        return option

    def complete1stMyAffiliateAccountForm(self, name, web, tax):
        self.driver.find_element(*AffiliateAccountLocators.companyField).clear()
        self.driver.find_element(*AffiliateAccountLocators.companyField).send_keys(name)
        self.driver.find_element(*AffiliateAccountLocators.websiteField).clear()
        self.driver.find_element(*AffiliateAccountLocators.websiteField).send_keys(web)
        self.driver.find_element(*AffiliateAccountLocators.taxIdField).clear()
        self.driver.find_element(*AffiliateAccountLocators.taxIdField).send_keys(tax)
        #self.driver.find_element(*AffiliateAccountLocators.checkboxAboutUs).click()

    def complete2ndMyAffiliateAccountCheque(self, chequeName):
        self.driver.find_element(*AffiliateAccountLocators.chequePayeNameField).send_keys(chequeName)


    def complete2ndMyAffiliateAccountPayel(self, payelEmail):
        self.driver.find_element(*AffiliateAccountLocators.paypelEmailAccountField).send_keys(payelEmail)

    def complete2ndMyAffiliateAccountBank(self, bankName, branch, swift, name, number):
        self.driver.find_element(*AffiliateAccountLocators.bankNameField).clear()
        self.driver.find_element(*AffiliateAccountLocators.bankNameField).send_keys(bankName)
        self.driver.find_element(*AffiliateAccountLocators.branchNumberField).clear()
        self.driver.find_element(*AffiliateAccountLocators.branchNumberField).send_keys(branch)
        self.driver.find_element(*AffiliateAccountLocators.swiftCodeField).clear()
        self.driver.find_element(*AffiliateAccountLocators.swiftCodeField).send_keys(swift)
        self.driver.find_element(*AffiliateAccountLocators.accountNameField).clear()
        self.driver.find_element(*AffiliateAccountLocators.accountNameField).send_keys(name)
        self.driver.find_element(*AffiliateAccountLocators.accountNumberField).clear()
        self.driver.find_element(*AffiliateAccountLocators.accountNumberField).send_keys(number)




