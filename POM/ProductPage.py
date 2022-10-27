import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ProductPageLocators:
    iMacProduct = (By.CSS_SELECTOR, "#content  button:nth-child(1)>span")
    monitor941 = (By.CSS_SELECTOR, "#content>div>div:nth-child(2) button:nth-child(1)>span")
    monitorCinema = (By.CSS_SELECTOR, "#content>div:nth-child(5)>div:nth-child(1) button:nth-child(1)>span")
    confirmMonitorCinema = (By.CSS_SELECTOR, "#content>div:nth-child(3)>div:nth-child(1) button:nth-child(1)>span")
    listOfMp3Players = (By.CSS_SELECTOR, "#content div>ul a")
    imacWishList = (By.CSS_SELECTOR, "#content div.button-group>button:nth-child(2)")
    imacProductAddCartBtn = (By.CSS_SELECTOR, "#content div.button-group>button:nth-child(1)")
    individualCameraPrice = (By.CSS_SELECTOR, "#content>div:nth-child(3) span.price-tax")
    leftMenuOption = (By.CSS_SELECTOR, "#column-left>div.list-group>a")

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def addImacPhoneToCart(self):
        self.driver.find_element(*ProductPageLocators.iMacProduct).click()

    def addMonitor941ToCart(self):
        self.driver.find_element(*ProductPageLocators.monitor941).click()
        self.driver.find_element(*ProductPageLocators.monitorCinema).click()
        time.sleep(1)
        self.driver.find_element(*ProductPageLocators.confirmMonitorCinema).click()

    def getMP3PlayersList(self):
        return self.driver.find_elements(*ProductPageLocators.listOfMp3Players)

    def addImacToWishList(self):
        self.driver.find_element(*ProductPageLocators.imacWishList).click()

    def addImacProductToCart(self):
        self.driver.find_element(*ProductPageLocators.imacProductAddCartBtn).click()

    def showIndividualCamerasPrice(self):
        return self.driver.find_elements(*ProductPageLocators.individualCameraPrice)

    def showTotalItemsOnLeftMenu(self):
        return self.driver.find_elements(*ProductPageLocators.leftMenuOption)




