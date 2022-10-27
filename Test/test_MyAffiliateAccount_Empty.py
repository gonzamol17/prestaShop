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
class TestMyAffiliateEmpty(BaseClass):

    def test_MyAffiliateAccount_Empty(self):
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
        afap.selectBtnContinue()
        assert "Warning: You must agree to the About Us!" == afap.showErrorAboutUs()
        print("Se está mostrando el error correcto, ya que no se ha tildado el checkbox de About Us")
        time.sleep(2)
