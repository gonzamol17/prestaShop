import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.LoginPage import LoginPage
from POM.ProductPage import ProductPage
from POM.ShoppingCartPage import ShoppingCartPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestAddNewItemToCart(BaseClass):

    def test_AddNewItemToCart(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        tm.select_DesktopsMacOption()
        pp = ProductPage(driver)
        pp.addImacPhoneToCart()
        tm.select_ComponentsMonitors()
        pp.addMonitor941ToCart()
        tm.select_ShoppingCartLink()
        scp = ShoppingCartPage(driver)
        print("La cantidad de productos en el carrito es de : " + str(scp.showQuantityOfProducts()))
        time.sleep(3)
