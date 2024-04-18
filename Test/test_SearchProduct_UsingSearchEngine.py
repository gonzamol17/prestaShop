import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.LoginPage import LoginPage
from POM.ProductSearchPage import ProductSearchPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestSearchAProduct(BaseClass):

    def test_SearchAProduct(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.writeSearchedWord("iMac")
        psp = ProductSearchPage(driver)
        assert "iMac" == psp.getTitleItemProductSearched()
        print("Se ha encontrado el producto buscado: "+psp.getTitleItemProductSearched())
        time.sleep(3)
