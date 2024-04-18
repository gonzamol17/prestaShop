#hacer login-list
#luego seleccionar del top menu page la opción Cameras-listo
#Luego verificar que cada producto mostrado tenga el valor en dolares (valor por defecto)-listo
#luego hacer click en currency menú izquierzo superior y cambiar a libras esterlinas-listo
#y verificar que en cada producto ahora muestre el simbolo libras-falta

import time
import pytest
import unittest
import sys
import os

from POM.AccountPage import AccountPage
from POM.LoginPage import LoginPage
from POM.ProductPage import ProductPage
from POM.TopMenuPage import TopMenuPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass


class TestEmptyCart(BaseClass):

    def test_Verify_Empty_Cart(self):
        log = self.get_Logger()
        driver = self.driver
        tm = TopMenuPage(driver)
        tm.select_LoginOption()
        lp = LoginPage(driver)
        lp.tryLoginUser("gonzalo.molina@darwoft.com", "Maestruli10")
        tm.selectCamerasOption()
        driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        pp = ProductPage(driver)
        price = pp.showIndividualCamerasPrice()
        list1 = []
        for i in price:
            list1.append(i.text)
            assert "$" in i.text
            #print(i.text)
        driver.execute_script("window.scrollTo(0, 200)")
        tm.selectChangeCurrencyOption()
        tm.selectPoundSterlingCurrency()
        driver.execute_script("window.scrollTo(0, 300)")
        price = pp.showIndividualCamerasPrice()
        list2 = []
        for m in price:
            list2.append(m.text)
            assert "£" in m.text
            #print(m.text)
        if list1 == list2:
            print("No se ha cambiado de moneda")
        else:
            print("Se ha cambiado de moneda exitosamente, y ahora se visualiza los productos con moneda en Libras Esterlinas")
            print("Lista 1, con productos con Moneda Dólares por defecto:")
            print(list1)
            print("Lista 2, una vez que se cambió la moneda, ahora los productos, se visualizan con Libras Esterlinas:")
            print(list2)
        time.sleep(3)
