import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.LoginPage import LoginPage
from POM.ShoppingCartPage import ShoppingCartPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestCleanShoppingCart(BaseClass):

    def test_CleanShoppingCart(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        tm.select_ShoppingCartLink()
        scp = ShoppingCartPage(driver)
        try:
            assert "Your shopping cart is empty!" == scp.verifyShoppingCartIsEmpty()

        except:
            print("La cantidad de productos en el carrito a eliminar es: " + str(scp.showQuantityOfProducts()))
            scp.clean_List_Of_Products()
            time.sleep(2)
            print("Ahora si se visualiza el mensaje: "+scp.verifyShoppingCartIsEmpty())
        time.sleep(3)
