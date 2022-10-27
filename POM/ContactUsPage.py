import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ContactUsPageLocators:
    titleContactUs = (By.CSS_SELECTOR, "#content>h1")
    txt_Name = (By.ID, "input-name")
    txt_Email = (By.ID, "input-email")
    txt_Enquiry = (By.ID, "input-enquiry")
    btn_Submit = (By.CSS_SELECTOR, "#content>form>div input")
    btnContinue = (By.CSS_SELECTOR, "#content>div>div>a")



class ContactUsPage:

    def __init__(self, driver):
        self.driver = driver


    def showTitleContactUs(self):
        return self.driver.find_element(*ContactUsPageLocators.titleContactUs).text

    def showNameFilled(self):
        return self.driver.find_element(*ContactUsPageLocators.txt_Name).get_attribute("value")

    def showEmailFilled(self):
        return self.driver.find_element(*ContactUsPageLocators.txt_Email).get_attribute("value")

    def completeDescription(self, text):
        self.driver.find_element(*ContactUsPageLocators.txt_Enquiry).send_keys(text)

    def selectBtnSendForm(self):
        self.driver.find_element(*ContactUsPageLocators.btn_Submit).click()

    def verifyBtnSuccessSendMessage(self):
        return self.driver.find_element(*ContactUsPageLocators.btnContinue)

