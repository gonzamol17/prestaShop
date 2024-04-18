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
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestLoginUser(BaseClass):

    def test_LoginUser(self):
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
        time.sleep(10)
