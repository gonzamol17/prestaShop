import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.FooterPage import FooterPage
from POM.LoginPage import LoginPage
from POM.TopMenuPage import TopMenuPage
from POM.GiftCertificatePage import GiftCertificatePage
from POM.CheckoutPage import CheckoutPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestCreateGiftCertificates(BaseClass):

    def test_Create_Gift_Certificates(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        driver.execute_script("window.scrollTo(0, 500)")
        fp = FooterPage(driver)
        fp.selectLinkGiftCertificates()
        gp = GiftCertificatePage(driver)
        assert "This gift certificate" in gp.showTitleGiftCertificate()
        assert "gonzalo lopez" == gp.verifyTheCorrectUserName()
        amount = 100
        gp.completeAllForm("Pedro1", "Pedro1@gmail.com", "Esta es la segunda prueba", amount)
        assert "Thank you for purchasing a gift certificate!" in gp.showTitleSuccessGiftCreated()
        gp.selectBtnContinueAndCheckout()
        cp = CheckoutPage(driver)
        assert "Checkout" == cp.showTitleAccountPage()
        cp.selectBtnContinueCheckoutGift("Este es el primer ejemplo")
        time.sleep(2)
        assert "Your order has been placed!" == cp.showSuccessTitleTransaction()
        cp.selectBtnContinueGiftConfirmation()
        fp.selectLinkOrderHistory()
        time.sleep(2)


