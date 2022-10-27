import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TopMenuPageLocators:
    myAccountLink = (By.XPATH, "//span[contains(text(),'My Account')]")
    loginOption = (By.XPATH, "//li/a[contains(text(),'Login')]")
    registerOption = (By.XPATH, "//a[contains(text(),'Register')]")
    txtSearchField = (By.CSS_SELECTOR, "#search>input")
    logOutOption = (By.CSS_SELECTOR, "#top-links>ul ul>li:nth-child(5)>a")
    myAccountLink1 = (By.CSS_SELECTOR, "#top-links li.dropdown span.hidden-xs.hidden-sm.hidden-md")
    btnContinue = (By.CSS_SELECTOR, "#content>div>div>a")
    shoppingCartLink = (By.CSS_SELECTOR, "#top-links>ul>li:nth-child(4)>a>span")
    desktopsOption = (By.CSS_SELECTOR, "#menu>div.collapse.navbar-collapse.navbar-ex1-collapse>ul>li:nth-child(1)>a")
    macOption = (By.CSS_SELECTOR, "#menu li:nth-child(1) li:nth-child(2)>a")
    componentsOption = (By.CSS_SELECTOR, "#menu>div.collapse.navbar-collapse.navbar-ex1-collapse>ul>li:nth-child(3)>a")
    monitorsOption = (By.CSS_SELECTOR, "#menu li:nth-child(3) li:nth-child(2)>a")
    lblSearchEngine = (By.CSS_SELECTOR, "#search>input")
    btnSearchEngine = (By.CSS_SELECTOR, "#search>span>button")
    mp3PlayersOption = (By.CSS_SELECTOR, "#menu ul>li:nth-child(8)>a")
    seeAllMp3PlayersOption = (By.CSS_SELECTOR, "#menu ul>li:nth-child(8)>div>a")
    wishListOption = (By.CSS_SELECTOR, "#wishlist-total>span")
    totalWishListProduct = (By.CSS_SELECTOR, "#wishlist-total>span")
    addCartBtn = (By.ID, "cart")
    optionCheckout = (By.CSS_SELECTOR, "#cart a:nth-child(2)>strong")
    barMenu = (By.CSS_SELECTOR, ".navbar-nav>li>a")
    btnTotalCart = (By.CSS_SELECTOR, "#cart-total")
    lblEmptyCart = (By.CSS_SELECTOR, "#cart>ul>li>p")
    camerasOption = (By.CSS_SELECTOR, "#menu ul>li:nth-child(7)>a")
    changeCurrencyOption = (By.CSS_SELECTOR, "#form-currency>div>button>span")
    poundSterlingCurrency = (By.CSS_SELECTOR, "#form-currency li:nth-child(2)>button")



class TopMenuPage:

    def __init__(self, driver):
        self.driver = driver


    def select_LoginOption(self):
        #hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*TopMenuPageLocators.myAccountLink))
        #hover.perform()
        #time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.myAccountLink).click()
        time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.loginOption).click()
        time.sleep(3)


    def select_RegisterOption(self):
        #hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*TopMenuPageLocators.myAccountLink))
        #hover.perform()
        #time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.myAccountLink).click()
        time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.registerOption).click()
        time.sleep(3)

    def select_LogOff(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*TopMenuPageLocators.myAccountLink1))
        hover.perform()
        time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.myAccountLink1).click()
        time.sleep(2)
        self.driver.find_element(*TopMenuPageLocators.logOutOption).click()
        self.driver.find_element(*TopMenuPageLocators.btnContinue).click()


    def select_ShoppingCartLink(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*TopMenuPageLocators.shoppingCartLink))
        hover.perform()
        time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.shoppingCartLink).click()

    def select_DesktopsMacOption(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*TopMenuPageLocators.desktopsOption))
        hover.perform()
        time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.macOption).click()

    def select_ComponentsMonitors(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*TopMenuPageLocators.componentsOption))
        hover.perform()
        time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.monitorsOption).click()

    def writeSearchedWord(self, product):
        self.driver.find_element(*TopMenuPageLocators.lblSearchEngine).send_keys(product)
        time.sleep(2)
        self.driver.find_element(*TopMenuPageLocators.btnSearchEngine).click()

    def select_Mp3Players(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*TopMenuPageLocators.mp3PlayersOption))
        hover.perform()
        time.sleep(3)
        self.driver.find_element(*TopMenuPageLocators.seeAllMp3PlayersOption).click()

    def select_WishListOption(self):
        self.driver.find_element(*TopMenuPageLocators.wishListOption).click()

    def getTotalWishListProduct(self):
        return self.driver.find_element(*TopMenuPageLocators.totalWishListProduct).text

    def addProductToCart(self):
        self.driver.find_element(*TopMenuPageLocators.addCartBtn).click()

    def goCheckoutOption(self):
        self.driver.find_element(*TopMenuPageLocators.optionCheckout).click()

    def showAllBarMenu(self):
        return self.driver.find_elements(*TopMenuPageLocators.barMenu)

    def showEmptyCart(self):
        return self.driver.find_element(*TopMenuPageLocators.btnTotalCart).text

    def showLblEmptyCart(self):
        return self.driver.find_element(*TopMenuPageLocators.lblEmptyCart).text

    def selectCamerasOption(self):
        self.driver.find_element(*TopMenuPageLocators.camerasOption).click()

    def selectChangeCurrencyOption(self):
        self.driver.find_element(*TopMenuPageLocators.changeCurrencyOption).click()

    def selectPoundSterlingCurrency(self):
        self.driver.find_element(*TopMenuPageLocators.poundSterlingCurrency).click()

