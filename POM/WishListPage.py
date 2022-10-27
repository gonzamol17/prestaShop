import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class WishListLocators:
    titleEmptyWishList = (By.CSS_SELECTOR, "#content>p")
    removeProduct = (By.CSS_SELECTOR, "#content tr>td:nth-child(6)>a")
    btnContinue = (By.CSS_SELECTOR, "#content>div>div>a")



class WishListPage:

    def __init__(self, driver):
        self.driver = driver


    def showTitleEmptyWishList(self):
        return self.driver.find_element(*WishListLocators.titleEmptyWishList).text

    def removeItemWishList(self):
        self.driver.find_element(*WishListLocators.removeProduct).click()

    def selectContinueBtn(self):
        self.driver.find_element(*WishListLocators.btnContinue).click()


