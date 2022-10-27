import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class RegisterAccountPageLocators:
    txtFirstNameBox = (By.ID, "input-firstname")
    txtLastNameBox = (By.ID, "input-lastname")
    txtEmailBox = (By.ID, "input-email")
    txtTelephoneBox = (By.ID, "input-telephone")
    txtPasswordBox = (By.ID, "input-password")
    #txtConfirmPassBox = (By.ID, "input-confirm")
    checkboxPolicy = (By.CSS_SELECTOR, "#form-register>div>div>div>input")
    btnContinue = (By.CSS_SELECTOR, "#form-register>div>div>button")



class RegisterAccountPage:

    def __init__(self, driver):
        self.driver = driver


    def completeMandatoryFields(self, name, last, email, password):
        #if gender.lower() == "mr":
        #    self.driver.find_element(*RegisterAccountPageLocators.radioButtonMr).click()
        #elif gender.lower() == "mrs":
        #    self.driver.find_element(*RegisterAccountPageLocators.radioButtonMrs).click()
        self.driver.find_element(*RegisterAccountPageLocators.txtFirstNameBox).send_keys(name)
        self.driver.find_element(*RegisterAccountPageLocators.txtLastNameBox).send_keys(last)
        self.driver.find_element(*RegisterAccountPageLocators.txtEmailBox).send_keys(email)
        #self.driver.find_element(*RegisterAccountPageLocators.txtTelephoneBox).send_keys(telephone)
        self.driver.find_element(*RegisterAccountPageLocators.txtPasswordBox).send_keys(password)
        #self.driver.find_element(*RegisterAccountPageLocators.txtConfirmPassBox).send_keys(repassword)
        self.driver.find_element(*RegisterAccountPageLocators.checkboxPolicy).click()
        self.driver.find_element(*RegisterAccountPageLocators.btnContinue).click()

