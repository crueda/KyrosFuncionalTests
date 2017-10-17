#!/usr/bin/env python
# -*- coding: utf-8 -*-

# autor: Carlos Rueda
# date: 2017-10-17
# mail: carlos.rueda@deimos-space.com
# version: 1.0

##################################################################################
# version 1.0 release notes:
# Initial version
# Requisites: 
#       libary selenium                To install: "pip install -U selenium"
##################################################################################

# TEST DE LOGIN EN KYROS-VIEW

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging, logging.handlers
from selenium.webdriver.support.ui import Select

#### VARIABLES #########################################################
from configobj import ConfigObj
config = ConfigObj('/Users/Carlos/Workspace/Kyros/KyrosFuncionalTests/tests.properties')
#config = ConfigObj('/home/acceso/scripts/tests.properties')


LOG_FILE = config['log_folder'] + "/tests.log"
LOG_FOR_ROTATE = 10

RESULTS_FILE = config['result_file_test004_chrome']

URL = config['url_view']
USERNAME = config['username']
PASSWORD = config['password']

CHROME_DRIVER = config['chrome_driver']


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
        'subtest_1': 1,  # login ok
        'subtest_2': 1,  # nuevo informe automatico

    }
    n_test_ok = 0
    n_test_error = 0

    def setUp(self):
        self.browser = webdriver.Chrome(CHROME_DRIVER)
        
    def test002(self):
        logger.info("Opening Chrome browser and open URL...")
        browser = self.browser
       
        #subtest_1
        logger.info("Launching subtest 1...")
        try:
            browser.get(URL)
            time.sleep(1)
            username = browser.find_element_by_name("user")
            password = browser.find_element_by_name("pass")
            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)
            password.send_keys(Keys.RETURN)
            time.sleep(5)
            
            #comprobar si esta el boton de menu
            logger.debug("Buscar en el combo el username")
            if '<div id="attr-button-menu" class="attr-button-menu" onclick="javascript:openMenuKyros();"></div>' in browser.page_source: 
                self.test_results['subtest_1'] = 0

            #logout

        except Exception as error:
            logger.error("Error at subtest_1: %s", str(error))
            self.test_results['subtest_1'] = 1
            self.n_test_error += 1
            self.test_result_code = 2        
            #pass

        try:
            #logout
            browser.find_element_by_id("attr-button-menu").click()
            time.sleep(1)
            browser.find_element_by_id("button-salir").click()
            time.sleep(1)
            self.test_results['subtest_2'] = 0

        except Exception as error:
            logger.error("Error at subtest_1: %s", str(error))
            self.test_results['subtest_2'] = 1
            self.n_test_error += 1
            self.test_result_code = 2
            #pass

        # Volcar la salida a fichero
        results_file = open(RESULTS_FILE,'w') 
        results_file.write (str(time.strftime("%d/%m/%y - %I:%M:%S")) + "," + str(self.test_result_code) + "," + str(self.n_test_ok) + "," + str(self.n_test_error) + "," + str(self.test_results['subtest_1']) + "," + str(self.test_results['subtest_2'])  )
        results_file.close()

    def tearDown(self):
        logger.info("Closing Chrome browser...")
        self.browser.close()
        logger.debug("OK!")

if __name__ == "__main__":
    unittest.main()
