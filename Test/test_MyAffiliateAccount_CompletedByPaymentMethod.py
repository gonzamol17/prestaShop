import time
import pytest
import unittest
import sys
import os

from POM.FooterPage import FooterPage
from POM.AccountPage import AccountPage
from POM.LoginPage import LoginPage
from POM.AffiliateAccountPage import AffiliateAccountPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestMyAffiliateCompletedByPaymentMethod(BaseClass):

    def test_MyAffiliateAccount_CompletedByPaymentMethod(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        fp = FooterPage(driver)
        fp.selectLinkMyAccount()
        driver.execute_script("window.scrollTo(0, 300)")
        ap = AccountPage(driver)
        ap.selectAffiliateAccount()
        afap = AffiliateAccountPage(driver)
        afap.complete1stMyAffiliateAccountForm("pepe company", "www.pepe.com.ar", "1200")
        value = afap.selectPaymentMethodOption("bank")
        if value == "cheque":
            afap.complete2ndMyAffiliateAccountCheque("Gonzalo")
        elif value == "paypal":
            afap.complete2ndMyAffiliateAccountPayel("pepe.bus@hotmail.com")
        else:
            afap.complete2ndMyAffiliateAccountBank("Santander", "capital", "1234", "Lorenzo", "Bermudez")
        time.sleep(5)
        afap.selectBtnContinue()
