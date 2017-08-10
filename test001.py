#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Test001(unittest.TestCase):

    test_result_code = 0 # 0=0k, 1=warning, 2=error
    test_results = {
        'subtest_1': 0, # Titulo 'Kyros' en el navegador
        'subtest_2': 0, # Idioma ruso
        'subtest_3': 0, # Idioma portugues
        'subtest_4': 0, # Idioma aleman
        'subtest_5': 0, # Idioma frances
        'subtest_6': 0, # Idioma ingles
        'subtest_7': 0, # Idioma español
        'subtest_8': 0, # Login pulsando enter en el campo username
        'subtest_9': 0, # Login pulsando enter en el campo password
        'subtest_10': 0  # Login pulsando sobre el botón de login
    }

    def setUp(self):
        self.browser = webdriver.Chrome("/Applications/chromedriver")

    def test001(self):
        browser = self.browser
        browser.get("https://demos.kyroslbs.com")
        time.sleep(1)

        #subtest_1
        if "Kyros" not in browser.title:
            self.test_results['subtest_1'] = 1
            self.test_result_code = 1

        #subtest_5
        button_fr = browser.find_element_by_xpath("//img[contains(@src, 'fr.png')]") 
        button_fr.click()
        time.sleep(1)
        if "votre mot de passe" not in browser.page_source: 
            self.test_results['subtest_5'] = 1
            self.test_result_code = 1

        username = browser.find_element_by_name("user")
        password = browser.find_element_by_name("password")
        username.send_keys("crueda")
        password.send_keys("dat1234")
        password.send_keys(Keys.RETURN)
        time.sleep(1)
        if "proporcionada" in browser.page_source:
            self.test_results['subtest_3'] = 1
            self.test_result_code = 2

        print self.test_result_code
        print self.test_results

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
