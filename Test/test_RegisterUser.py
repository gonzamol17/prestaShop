import time
import pytest
import unittest
import sys
import os

from POM.RegisterAccountPage import RegisterAccountPage
from POM.LoginPage import LoginPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestRegisterUser(BaseClass):

    def test_RegisterUser(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_RegisterOption()
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(3)
        rap = RegisterAccountPage(driver)
        rap.completeMandatoryFields("Gonzalo", "Molina", "gonzalo.molina@darwoft.com", "Maestruli10")
        time.sleep(3)
