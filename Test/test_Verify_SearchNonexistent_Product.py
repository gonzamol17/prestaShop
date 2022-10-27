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
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestSearchANonExistentProduct(BaseClass):

    def test_SearchANonExistentProduct(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.writeSearchedWord("pato")
        psp = ProductSearchPage(driver)
        assert "Your shopping cart is empty!" == psp.getTitleNonExistentProductSearched()
        print("No existe en el sistema, el producto buscado")
        time.sleep(3)
