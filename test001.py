#!/usr/bin/env python
# -*- coding: utf-8 -*-

# autor: Carlos Rueda
# date: 2017-08-10
# mail: carlos.rueda@deimos-space.com
# version: 1.0

##################################################################################
# version 1.0 release notes:
# Initial version
# Requisites: 
#       libary selenium                To install: "pip install -U selenium"
##################################################################################

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging, logging.handlers

#### VARIABLES #########################################################
from configobj import ConfigObj
config = ConfigObj('./tests.properties')

LOG_FILE = config['log_folder'] + "/tests.log"
LOG_FOR_ROTATE = 10

RESULTS_FILE = config['result_file_test001']

URL = config['url']
USERNAME = config['username']
PASSWORD = config['password']

#### LOGGER #########################################################
try:
    logger = logging.getLogger('tests')
    loggerHandler = logging.handlers.TimedRotatingFileHandler(LOG_FILE, 'midnight', 1, backupCount=LOG_FOR_ROTATE)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    loggerHandler.setFormatter(formatter)
    logger.addHandler(loggerHandler)
    logger.setLevel(logging.DEBUG)
except:
    print '------------------------------------------------------------------'
    print '[ERROR] Error writing log at %s' % LOG_FILE
    print '[ERROR] Please verify path folder exits and write permissions'
    print '------------------------------------------------------------------'
    exit()
########################################################################

#### FUNCTIONS #########################################################
def format(string):
    try:
        return string.encode('utf-8')
    except:
        pass
        return string

class Test001(unittest.TestCase):

    test_result_code = 0 # 0=0k, 1=warning, 2=error
    test_results = {
        'subtest_1': 1, # Titulo 'Kyros' en el navegador
        'subtest_2': 1, # Idioma ruso
        'subtest_3': 1, # Idioma portugues
        'subtest_4': 1, # Idioma aleman
        'subtest_5': 1, # Idioma frances
        'subtest_6': 1, # Idioma ingles
        'subtest_7': 1, # Idioma español
        'subtest_8': 1, # Login pulsando enter en el campo username
        'subtest_9': 1, # Login pulsando enter en el campo password
        'subtest_10': 1  # Login pulsando sobre el botón de login
    }

    def setUp(self):
        self.browser = webdriver.Chrome("/Applications/chromedriver")

    def test001(self):
        logger.info("Opening Chrome browser and open URL...")
        browser = self.browser
        browser.get("https://demos.kyroslbs.com")
        logger.debug("OK!")
        time.sleep(1)

        #subtest_1
        logger.info("Launching subtest 1...")
        try:
            if "Kyros" in browser.title:
                self.test_results['subtest_1'] = 0
            else:
                self.test_results['subtest_1'] = 1
                self.test_result_code = 1
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_1: %s", str(error))
            pass

        #subtest_2
        logger.info("Launching subtest 2...")
        try:
            button_ru = browser.find_element_by_xpath("//img[contains(@src, 'rs.png')]") 
            button_ru.click()
            time.sleep(1)
            if format("Забыли пароль") in format(browser.page_source): 
                self.test_results['subtest_2'] = 0
            else:
                self.test_results['subtest_2'] = 1
                self.test_result_code = 1
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_2: %s", str(error))
            pass

        #subtest_3
        logger.info("Launching subtest 3...")
        try:
            button_pt = browser.find_element_by_xpath("//img[contains(@src, 'pt.png')]") 
            button_pt.click()
            time.sleep(1)
            if format("esqueceu sua senha") in browser.page_source: 
                self.test_results['subtest_3'] = 0
            else:
                self.test_results['subtest_3'] = 1
                self.test_result_code = 1
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_3: %s", str(error))
            pass

        #subtest_4
        logger.info("Launching subtest 4...")
        try:
            button_de = browser.find_element_by_xpath("//img[contains(@src, 'de.png')]") 
            button_de.click()
            time.sleep(1)
            if format("Passwort vergessen") in browser.page_source: 
                self.test_results['subtest_4'] = 0
            else:
                self.test_results['subtest_4'] = 1
                self.test_result_code = 1
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_4: %s", str(error))
            pass

        #subtest_5
        logger.info("Launching subtest 5...")
        try:
            button_fr = browser.find_element_by_xpath("//img[contains(@src, 'fr.png')]") 
            button_fr.click()
            time.sleep(1)
            if format("votre mot de passe") in browser.page_source: 
                self.test_results['subtest_5'] = 0
            else:
                self.test_results['subtest_5'] = 1
                self.test_result_code = 1
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_5: %s", str(error))
            pass

        #subtest_6
        logger.info("Launching subtest 6...")
        try:
            button_en = browser.find_element_by_xpath("//img[contains(@src, 'en.png')]") 
            button_en.click()
            time.sleep(1)
            if format("Forgot your password") in browser.page_source: 
                self.test_results['subtest_6'] = 0
            else:
                self.test_results['subtest_6'] = 1
                self.test_result_code = 1
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_6: %s", str(error))
            pass

        #subtest_7
        logger.info("Launching subtest 7...")
        try:
            button_es = browser.find_element_by_xpath("//img[contains(@src, 'es.png')]") 
            button_es.click()
            time.sleep(1)
            if format("Olvidó su contraseña") in format(browser.page_source): 
                self.test_results['subtest_7'] = 0
            else:
                self.test_results['subtest_7'] = 1
                self.test_result_code = 1
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_6: %s", str(error))
            pass

        #subtest_8
        logger.info("Launching subtest 8...")
        try:
            username = browser.find_element_by_name("user")
            password = browser.find_element_by_name("password")
            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)
            username.send_keys(Keys.RETURN)
            time.sleep(1)
            if "proporcionada" not in browser.page_source:
                self.test_results['subtest_8'] = 0
                button = browser.find_element_by_class_name('logoutIcon')
                button.click()
                time.sleep(1)
                button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
                button[0].click()
                time.sleep(2)
            else:
                self.test_results['subtest_8'] = 1
                self.test_result_code = 2
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_8: %s", str(error))
            pass

        #subtest_9
        logger.info("Launching subtest 9...")
        try:
            browser.get("https://demos.kyroslbs.com")
            time.sleep(1)
            username = browser.find_element_by_name("user")
            password = browser.find_element_by_name("password")
            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)
            password.send_keys(Keys.RETURN)
            time.sleep(1)
            if "proporcionada" not in browser.page_source:
                self.test_results['subtest_9'] = 0
                button = browser.find_element_by_class_name('logoutIcon')
                button.click()
                time.sleep(1)
                button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
                button[0].click()
                time.sleep(2)
            else:
                self.test_results['subtest_9'] = 1
                self.test_result_code = 2
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_9: %s", str(error))
            pass

        #subtest_10
        logger.info("Launching subtest 10...")
        try:
            browser.get("https://demos.kyroslbs.com")
            time.sleep(1)
            username = browser.find_element_by_name("user")
            password = browser.find_element_by_name("password")
            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)
            button_login = browser.find_element_by_xpath("//img[contains(@src, 'transparent.png')]") 
            button_login.click()
            time.sleep(1)
            if "proporcionada" not in browser.page_source:
                self.test_results['subtest_10'] = 0
                button = browser.find_element_by_class_name('logoutIcon')
                button.click()
                time.sleep(1)
                button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
                button[0].click()
                time.sleep(2)
            else:
                self.test_results['subtest_10'] = 1
                self.test_result_code = 2
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_10: %s", str(error))
            pass

        # Volcar la salida a fichero
        results_file = open(RESULTS_FILE,'w') 
        results_file.write (str(self.test_result_code) + "," + str(self.test_results['subtest_1']) + "," + str(self.test_results['subtest_2']) + "," + str(self.test_results['subtest_3']) + "," + str(self.test_results['subtest_4']) + "," + str(self.test_results['subtest_5']) + "," + str(self.test_results['subtest_6']) + "," + str(self.test_results['subtest_7']) + "," + str(self.test_results['subtest_8']) + "," + str(self.test_results['subtest_9']) + "," + str(self.test_results['subtest_10']))
        results_file.close()

    def tearDown(self):
        logger.info("Closing Chrome browser...")
        self.browser.close()
        logger.debug("OK!")

if __name__ == "__main__":
    unittest.main()
