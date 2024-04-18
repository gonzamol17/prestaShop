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
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestCompleteContactUs(BaseClass):

    def test_CompleteContactUs_Form(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        driver.execute_script("window.scrollTo(0, 500)")
        fp = FooterPage(driver)
        time.sleep(3)
        fp.selectLinkContactUs()
        time.sleep(3)
        cup = ContactUsPage(driver)
        assert "Contact Us" == cup.showTitleContactUs()
        print("Estamos en la pantalla de Contact Us")
        driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(3)
        name = cup.showNameFilled()
        assert name != ""
        email = cup.showEmailFilled()
        assert email != ""
        print("El Nombre ingresado en el text box es: " + name)
        print("El Email ingresado en el text box es: " + email)
        cup.completeDescription("This is the first message to complete")
        cup.selectBtnSendForm()
        assert cup.verifyBtnSuccessSendMessage().is_displayed() == True
        print("Se pudo mandar exitosamente el formulario de Contact Us")
        time.sleep(3)
