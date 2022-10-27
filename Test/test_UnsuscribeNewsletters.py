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
class TestUnsuscribeNewsLetter(BaseClass):

    def test_UnsuscribeNewsLetter(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        ap = AccountPage(driver)
        assert "My Account" == ap.showTitleAccountPage()
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)
        ap.selectNewsLetterLink()
        if ap.showRadioButtonYesStatus():
            print("Como está habilitado la suscripción, se procederá a dar la baja en la suscripción")
            ap.selectNoSubscriptionOnNewsLetter()
            ap.selectContinueBtn()
            assert "successfully updated!" in ap.showSuccessUnsuscribeNewsLetter()
        else:
            print("Como ya está deshabilitada la suscripción, no se hace nada")
        time.sleep(3)
