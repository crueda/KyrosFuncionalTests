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

RESULTS_FILE = config['result_file_test002']

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

class Test002(unittest.TestCase):

    test_result_code = 0 # 0=0k, 1=warning, 2=error
    test_results = {
        'subtest_1': 1  # Crear flota
    }
    n_test_ok = 0
    n_test_error = 0

    def setUp(self):
        self.browser = webdriver.Chrome("/Applications/chromedriver")
        #self.browser = webdriver.Firefox("/Applications/geckodriver")
        #self.browser = webdriver.Safari()
        
    def test002(self):
        logger.info("Opening Chrome browser and open URL...")
        browser = self.browser
       
        #subtest_1
        logger.info("Launching subtest 1...")
        try:
            browser.get("https://demos.kyroslbs.com")
            time.sleep(1)
            username = browser.find_element_by_name("user")
            password = browser.find_element_by_name("password")
            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)
            #pulsar boton de login
            button_login = browser.find_element_by_xpath("//img[contains(@src, 'transparent.png')]") 
            button_login.click()
            time.sleep(1)
            #pulsar tab de administracion
            button = browser.find_element_by_class_name('adminIcon')
            button.click()
            time.sleep(1)
            #pulsar flotas
            button = browser.find_element_by_link_text('Flotas')
            button.click()
            time.sleep(1)
            #pulsar nueva flota
            #button = browser.find_element_by_xpath("//button[style='background-image: url(\"images/add.png\")']") 
            button = browser.find_elements_by_partial_link_text('Nueva')
            button.click()
            time.sleep(3)

            self.test_results['subtest_1'] = 0
            self.n_test_ok += 1
            logger.debug("OK!")
        except Exception as error:
            logger.error("Error at subtest_1: %s", str(error))
            self.test_results['subtest_1'] = 1
            self.n_test_error += 1
            self.test_result_code = 2
            #pass

        # Volcar la salida a fichero
        #results_file = open(RESULTS_FILE,'w') 
        #results_file.write (str(time.strftime("%d/%m/%y - %I:%M:%S")) + "," + str(self.test_result_code) + "," + str(self.n_test_ok) + "," + str(self.n_test_error) + "," + str(self.test_results['subtest_1']) + "," + str(self.test_results['subtest_2']) + "," + str(self.test_results['subtest_3']) + "," + str(self.test_results['subtest_4']) + "," + str(self.test_results['subtest_5']) + "," + str(self.test_results['subtest_6']) + "," + str(self.test_results['subtest_7']) + "," + str(self.test_results['subtest_8']) + "," + str(self.test_results['subtest_9']) + "," + str(self.test_results['subtest_10']))
        #results_file.close()

    def tearDown(self):
        logger.info("Closing Chrome browser...")
        #self.browser.close()
        logger.debug("OK!")

if __name__ == "__main__":
    unittest.main()
