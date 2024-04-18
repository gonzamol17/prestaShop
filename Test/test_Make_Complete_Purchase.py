import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.CheckoutPage import CheckoutPage
from POM.LoginPage import LoginPage
from POM.ProductPage import ProductPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestCompletePurchase(BaseClass):

    def test_MakeAPurchase(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        ap = AccountPage(driver)
        assert "My Account" == ap.showTitleAccountPage()
        print("Your are logged in")
        log.info("Now you are logged in")
        time.sleep(3)
        tm = TopMenuPage(driver)
        tm.select_DesktopsMacOption()
        time.sleep(3)
        pp = ProductPage(driver)
        pp.addImacProductToCart()
        time.sleep(3)
        tm.addProductToCart()
        time.sleep(3)
        tm.goCheckoutOption()
        time.sleep(3)
        chp = CheckoutPage(driver)
        assert "Checkout" == chp.showTitleAccountPage()
        time.sleep(3)
        print("Estamos en la pantalla de Checkout")
        chp.selectBtnContinueCheckout()
        time.sleep(3)
        assert "Your order has been successfully processed!" == chp.showSuccessMessageTransaction()
        print("La orden ha sido procesada con éxito")
        time.sleep(3)



