import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ShoppingCartPageLocators:
    rowsOfProducts = (By.CSS_SELECTOR, "#content>form tbody>tr")
    tableProducts = (By.CSS_SELECTOR, "#content>form>div>table>tbody")
    btnCleanProducts = (By.CSS_SELECTOR, "#content div>span>button.btn.btn-danger")
    lblShoppingCartEmpty = (By.CSS_SELECTOR, "#content>p")




class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver


    def showQuantityOfProducts(self):
        rows = len(self.driver.find_elements(*ShoppingCartPageLocators.rowsOfProducts))
        return rows

    def showNameOfProducts(self):
        return self.driver.find_element(*ShoppingCartPageLocators.rowsOfProducts)

    def clean_List_Of_Products(self):
        elements = len(self.driver.find_elements(*ShoppingCartPageLocators.rowsOfProducts))
        ele = self.driver.find_elements(*ShoppingCartPageLocators.tableProducts)
        num = len(self.driver.find_elements(*ShoppingCartPageLocators.tableProducts))
        for ele in range(1, elements+1):
            self.driver.find_element(*ShoppingCartPageLocators.btnCleanProducts).click()
            time.sleep(2)

    def verifyShoppingCartIsEmpty(self):
        return self.driver.find_element(*ShoppingCartPageLocators.lblShoppingCartEmpty).text
