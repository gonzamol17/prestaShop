import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.ContactUsPage import ContactUsPage
from POM.FooterPage import FooterPage
from POM.LoginPage import LoginPage
from POM.ShoppingCartPage import ShoppingCartPage
from POM.TopMenuPage import TopMenuPage
from POM.ProductPage import ProductPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestGetAllElementsFromLeftMenu(BaseClass):

    def test_Get_all_Elements_Left_Menu(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        tm = TopMenuPage(driver)
        tm.selectCamerasOption()
        pp = ProductPage(driver)
        tot = len(pp.showTotalItemsOnLeftMenu())
        items = pp.showTotalItemsOnLeftMenu()
        print("Existe la cantidad de: "+str(tot)+" items, listados en el menú izquierdo")
        print("Y los items listados son: (con sus cantidades)")
        for i in items:
            print(i.text)
        time.sleep(3)
