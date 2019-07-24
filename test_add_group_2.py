# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import unittest
from group import Group
from application import Application


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="nina", header="wert", footer="wertyu"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()

