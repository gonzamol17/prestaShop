import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.LoginPage import LoginPage
from POM.ProductPage import ProductPage
from POM.ProductSearchPage import ProductSearchPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestVerifyTheNumberOfMP3PlayerList(BaseClass):

    def test_VerifyTheMP3Playerslist(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_Mp3Players()
        pp = ProductPage(driver)
        listMP3= len(pp.getMP3PlayersList())
        print("Cantidad de items de mp3 son: "+str(listMP3))
        print("Y los productos listados son:")
        for i in pp.getMP3PlayersList():
            print("\n")
            print(i.text)
        time.sleep(3)
