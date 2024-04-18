import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.RegisterAccountPage import RegisterAccountPage
from POM.LoginPage import LoginPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestLogOut(BaseClass):

    def test_LogOut(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        ap = AccountPage(driver)
        assert "My Account" == ap.showTitleAccountPage()
        print("Your are logged in")
        time.sleep(3)
        tm.select_LogOff()
        print("Your are logged off")
        time.sleep(2)
