import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class FooterPageLocators:
    linkContactUs = (By.CSS_SELECTOR, "footer div:nth-child(2) li:nth-child(1)>a")
    linkGiftCertificates = (By.XPATH, "//a[contains(text(),'Gift Certificates')]")
    linkOrderHistory = (By.CSS_SELECTOR, "body>footer div:nth-child(4) li:nth-child(2)>a")
    linkMyAccount = (By.CSS_SELECTOR, "body>footer div:nth-child(4) li:nth-child(1)>a")


class FooterPage:

    def __init__(self, driver):
        self.driver = driver


    def selectLinkContactUs(self):
        self.driver.find_element(*FooterPageLocators.linkContactUs).click()

    def selectLinkGiftCertificates(self):
        self.driver.find_element(*FooterPageLocators.linkGiftCertificates).click()

    def selectLinkOrderHistory(self):
        self.driver.find_element(*FooterPageLocators.linkOrderHistory).click()

    def selectLinkMyAccount(self):
        self.driver.find_element(*FooterPageLocators.linkMyAccount).click()


