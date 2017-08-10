#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def format(string):
    try:
        return string.encode('utf-8')
    except:
        pass
        return string

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
        print "Opening Chrome browser and open URL..."
        browser = self.browser
        browser.get("https://demos.kyroslbs.com")
        print "OK!"
        time.sleep(1)

        print "Launching subtest 1..."
        #subtest_1
        if "Kyros" not in browser.title:
            self.test_results['subtest_1'] = 1
            self.test_result_code = 1
        print "OK!"

        #subtest_2
        button_ru = browser.find_element_by_xpath("//img[contains(@src, 'rs.png')]") 
        button_ru.click()
        time.sleep(1)
        if format("Забыли пароль") not in format(browser.page_source): 
            self.test_results['subtest_2'] = 1
            self.test_result_code = 1

        #subtest_3
        button_pt = browser.find_element_by_xpath("//img[contains(@src, 'pt.png')]") 
        button_pt.click()
        time.sleep(1)
        if format("esqueceu sua senha") not in browser.page_source: 
            self.test_results['subtest_3'] = 1
            self.test_result_code = 1

        #subtest_4
        button_de = browser.find_element_by_xpath("//img[contains(@src, 'de.png')]") 
        button_de.click()
        time.sleep(1)
        if format("Passwort vergessen") not in browser.page_source: 
            self.test_results['subtest_4'] = 1
            self.test_result_code = 1

        #subtest_5
        button_fr = browser.find_element_by_xpath("//img[contains(@src, 'fr.png')]") 
        button_fr.click()
        time.sleep(1)
        if format("votre mot de passe") not in browser.page_source: 
            self.test_results['subtest_5'] = 1
            self.test_result_code = 1

        #subtest_6
        button_en = browser.find_element_by_xpath("//img[contains(@src, 'en.png')]") 
        button_en.click()
        time.sleep(1)
        if format("Forgot your password") not in browser.page_source: 
            self.test_results['subtest_6'] = 1
            self.test_result_code = 1

        #subtest_7
        button_es = browser.find_element_by_xpath("//img[contains(@src, 'es.png')]") 
        button_es.click()
        time.sleep(1)
        if format("Olvidó su contraseña") not in format(browser.page_source): 
            self.test_results['subtest_7'] = 1
            self.test_result_code = 1

        #subtest_8
        username = browser.find_element_by_name("user")
        password = browser.find_element_by_name("password")
        username.send_keys("crueda")
        password.send_keys("dat1234")
        username.send_keys(Keys.RETURN)
        time.sleep(1)
        if "proporcionada" in browser.page_source:
            self.test_results['subtest_8'] = 1
            self.test_result_code = 2
        else:
            button = browser.find_element_by_class_name('logoutIcon')
            button.click()
            time.sleep(1)
            button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
            button[0].click()
            time.sleep(2)

        #subtest_9
        browser.get("https://demos.kyroslbs.com")
        time.sleep(1)
        username = browser.find_element_by_name("user")
        password = browser.find_element_by_name("password")
        username.send_keys("crueda")
        password.send_keys("dat1234")
        password.send_keys(Keys.RETURN)
        time.sleep(1)
        if "proporcionada" in browser.page_source:
            self.test_results['subtest_9'] = 1
            self.test_result_code = 2
        else:
            button = browser.find_element_by_class_name('logoutIcon')
            button.click()
            time.sleep(1)
            button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
            button[0].click()
            time.sleep(2)


        #subtest_10
        browser.get("https://demos.kyroslbs.com")
        time.sleep(1)
        username = browser.find_element_by_name("user")
        password = browser.find_element_by_name("password")
        username.send_keys("crueda")
        password.send_keys("dat1234")
        button_login = browser.find_element_by_xpath("//img[contains(@src, 'transparent.png')]") 
        button_login.click()
        time.sleep(1)
        if "proporcionada" in browser.page_source:
            self.test_results['subtest_10'] = 1
            self.test_result_code = 2
        else:
            button = browser.find_element_by_class_name('logoutIcon')
            button.click()
            time.sleep(1)
            button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
            button[0].click()
            time.sleep(2)

        print self.test_result_code
        print self.test_results

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
