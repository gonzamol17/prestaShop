import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.LoginPage import LoginPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestEmptyCart(BaseClass):

    def test_Verify_Empty_Cart(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        time.sleep(2)
        aux = tm.showEmptyCart()
        if aux == "0 item(s) - $0.00":
            time.sleep(2)
            tm.addProductToCart()
            assert tm.showLblEmptyCart() == "Your shopping cart is empty!"
            print("El carrito está vacío")
        time.sleep(3)
