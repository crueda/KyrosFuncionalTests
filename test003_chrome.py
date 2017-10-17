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
from selenium.webdriver.support.ui import Select

#### VARIABLES #########################################################
from configobj import ConfigObj
config = ConfigObj('/Users/Carlos/Workspace/Kyros/KyrosFuncionalTests/tests.properties')
#config = ConfigObj('/home/acceso/scripts/tests.properties')


LOG_FILE = config['log_folder'] + "/tests.log"
LOG_FOR_ROTATE = 10

RESULTS_FILE = config['result_file_test003_chrome']

URL = config['url']
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
        'subtest_1': 1,  # gestion de informes
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
            password = browser.find_element_by_name("password")
            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)
            #pulsar boton de login
            button_login = browser.find_element_by_xpath("//img[contains(@src, 'transparent.png')]") 
            button_login.click()
            time.sleep(5)
            #pulsar tab de gestion
            button = browser.find_element_by_class_name('manageIcon')
            button.click()
            time.sleep(3)
            #pulsar informes
            browser.find_elements_by_link_text('Informes')[1].click()
            time.sleep(1)
            #pulsar nuevo informe
            browser.find_elements_by_class_name("x-btn-text")[35].click()
            time.sleep(40)
            
            logger.debug("Buscar en el combo el username")
            if '<div class="x-combo-list-item">'+USERNAME+'</div>' in browser.page_source: 
                print "ESTA!"
            else:
                print "NO ESTA!"

            time.sleep(3)
            browser.find_elements_by_class_name("x-form-text")[9].send_keys(USERNAME)
            browser.find_elements_by_class_name("x-form-text")[9].send_keys(Keys.RETURN)
            time.sleep(3)


            print "****"
            inputs = browser.find_elements_by_link_text(USERNAME);            
            print "****2:" + str(len(inputs))
            i=0
            for element in inputs:
                print str(i) + ": " + element.text
                i+=1
            
            print "****3"
            


            
            time.sleep(1)

            self.test_results['subtest_1'] = 0
            self.n_test_ok += 1
            logger.debug("Gestión de informes -> OK!")


            
            
            '''
                self.test_results['subtest_2'] = 0
                self.n_test_ok += 1
                logger.debug("Crear nuevo informe automatico -> OK!")
            except Exception as error:
                logger.debug("Crear nuevo informe automatico -> Error")
                self.test_result_code = 1
                pass
            '''
            #pulsar nueva flota
            #buttons = browser.find_elements_by_class_name("x-btn-text");            
            #buttons[35].click()
            #time.sleep(1)
            
        

            #logout
            button = browser.find_element_by_class_name('logoutIcon')
            button.click()
            time.sleep(1)
            button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
            button[0].click()
            time.sleep(2)

        except Exception as error:
            logger.error("Error at subtest_1: %s", str(error))
            self.test_results['subtest_1'] = 1
            self.n_test_error += 1
            self.test_result_code = 2

            button = browser.find_element_by_class_name('logoutIcon')
            button.click()
            time.sleep(1)
            button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
            button[0].click()
            time.sleep(2)

            #pass

        # Volcar la salida a fichero
        #results_file = open(RESULTS_FILE,'w') 
        #results_file.write (str(time.strftime("%d/%m/%y - %I:%M:%S")) + "," + str(self.test_result_code) + "," + str(self.n_test_ok) + "," + str(self.n_test_error) + "," + str(self.test_results['subtest_1']) + "," + str(self.test_results['subtest_2']) + "," + str(self.test_results['subtest_3']) + "," + str(self.test_results['subtest_4']) + "," + str(self.test_results['subtest_5']) + "," + str(self.test_results['subtest_6']) )
        #results_file.close()

    def tearDown(self):
        logger.info("Closing Chrome browser...")
        #self.browser.close()
        logger.debug("OK!")

if __name__ == "__main__":
    unittest.main()
