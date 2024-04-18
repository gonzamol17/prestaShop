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
from POM.WishListPage import WishListPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestAddRemoveWishListProduct(BaseClass):

    def test_AddRemoveWishList(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        tm.select_WishListOption()
        wl = WishListPage(driver)
        try:
            assert "Your shopping cart is empty!" == wl.showTitleEmptyWishList()
            tm.select_DesktopsMacOption()
            time.sleep(2)
        except:
            time.sleep(2)
            wl.removeItemWishList()
            assert "Your shopping cart is empty!" == wl.showTitleEmptyWishList()
            wl.selectContinueBtn()
            time.sleep(2)
            tm.select_DesktopsMacOption()
        pp = ProductPage(driver)
        pp.addImacToWishList()
        time.sleep(1)
        aux = tm.getTotalWishListProduct()
        assert 'Wish List (1)' == aux
        print("Se agregó exitosamente el producto a la lista de deseos")
