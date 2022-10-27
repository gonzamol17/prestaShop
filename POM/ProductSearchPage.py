import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ProductSearchPageLocators:
    iMacItem = (By.CSS_SELECTOR, "#content div:nth-child(2)>div.caption>h4>a")
    emptyProductLabel = (By.CSS_SELECTOR, "#content>p:nth-child(7)")





class ProductSearchPage:

    def __init__(self, driver):
        self.driver = driver


    def getTitleItemProductSearched(self):
        return self.driver.find_element(*ProductSearchPageLocators.iMacItem).text

    def getTitleNonExistentProductSearched(self):
        return self.driver.find_element(*ProductSearchPageLocators.emptyProductLabel).text

