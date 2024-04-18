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
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestMyAffiliateWithoutChequePaye(BaseClass):

    def test_MyAffiliateAccount_WhitoutChequePaye(self):
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
        afap.selectAboutUs()
        afap.selectBtnContinue()
        assert "Cheque Payee Name required!" == afap.showErrorChequePaye()
        assert "rgba(169, 68, 66, 1)" == afap.showColorOfErrorChequePaye().value_of_css_property('color')
        print(Fore.RED +"Se está mostrando el error correcto, en color rojo, ya que no se ha cargado el label de Cheque Payee Name"+Fore.RESET)
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
