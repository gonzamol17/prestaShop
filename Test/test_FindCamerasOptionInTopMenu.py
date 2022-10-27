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

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass

@pytest.mark.usefixtures("test_setup")
class TestFindCamerasOptionInTopMenu(BaseClass):

    def test_FindCamerasOptionInTopMenu(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        name = tm.showAllBarMenu()
        num = 0
        for i in name:
            print(i.text)
            num = num + 1
            if i.text == 'Cameras':
                print("Se ha encontrado la opción Cameras, asique cortar la búsqueda")
                break
        if num == 7:
            print("Se imprimieron solamente "+str(num)+" números porque se encontro la opción Cameras")
        else:
            print("Se imprimieron todos los "+str(num)+" números porque no se encontro la opción Cameras")
        time.sleep(3)
