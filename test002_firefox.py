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
#config = ConfigObj('/Users/Carlos/Workspace/Kyros/KyrosFuncionalTests/tests.properties')
config = ConfigObj('/home/acceso/scripts/tests.properties')

LOG_FILE = config['log_folder'] + "/tests.log"
LOG_FOR_ROTATE = 10

RESULTS_FILE = config['result_file_test002_chrome']

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
        'subtest_1': 1,  # Crear flota
        'subtest_2': 1,  # Crear usuario de flota
        'subtest_3': 1,  # Login con el nuevo usuario
        'subtest_4': 1,  # Comprobar visualización de la flota
        'subtest_5': 1,  # Eliminar flota
        'subtest_6': 1  # Eliminar usuario
    }
    n_test_ok = 0
    n_test_error = 0

    def setUp(self):
        self.browser = webdriver.Firefox()
        
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
            #pulsar tab de administracion
            button = browser.find_element_by_class_name('adminIcon')
            button.click()
            time.sleep(1)
            #pulsar flotas
            button = browser.find_element_by_link_text('Flotas')
            button.click()
            time.sleep(1)
            #pulsar nueva flota
            buttons = browser.find_elements_by_class_name("x-btn-text");            
            buttons[35].click()
            time.sleep(1)
            inputs = browser.find_elements_by_class_name("x-form-text");            
            #Nombre de la flota
            logger.debug("Rellenar el nombre de la flota")
            inputs[10].send_keys("0-TEST002")
            #Seleccionar empresa:
            logger.debug("Rellenar el nombre de la empresa")
            consignor = browser.find_element_by_name("consignorId")
            consignor.send_keys("DEIMOS LBS")
            consignor.send_keys(Keys.RETURN)
            time.sleep(1)
            #comentario
            logger.debug("Rellenar el comentario")
            inputs[18].send_keys("Comentario de la flota para TEST002")
            
            #boton aceptar
            logger.debug("Pulsar el botón aceptar")
            buttons = browser.find_elements_by_class_name("x-btn-text");            
            buttons[42].click()          

            #boton 'si'
            browser.find_elements_by_class_name("x-btn-text")[42].click()
            time.sleep(1)

            #boton 'aceptar'
            browser.find_elements_by_class_name("x-btn-text")[37].click()

            self.test_results['subtest_1'] = 0
            self.n_test_ok += 1
            logger.debug("Creación de flota -> OK!")

            #pulsar Operadores Web
            button = browser.find_element_by_link_text('Operadores Web')
            button.click()
            time.sleep(2)

            #nuevo operador
            logger.debug("Pulsar el botón nuevo operador")
            browser.find_elements_by_class_name("x-btn-text")[43].click()
            time.sleep(1)
            
            '''
            inputs = browser.find_elements_by_class_name("x-form-text");            
            i=0
            for element in inputs:
                print str(i) + ": " + element.get_attribute("name")
                i+=1
            '''
            
            logger.debug("Rellenar el username")
            browser.find_elements_by_class_name("x-form-text")[19].send_keys("0-TEST002-user")
            logger.debug("Rellenar el firstname")
            browser.find_elements_by_class_name("x-form-text")[20].send_keys("TEST002-firstname")
            logger.debug("Rellenar el lastname")
            browser.find_elements_by_class_name("x-form-text")[21].send_keys("TEST002-lastname")
            logger.debug("Rellenar el correo")
            browser.find_elements_by_class_name("x-form-text")[22].send_keys("TEST002l@kyroslbs.com")
            logger.debug("Rellenar la contraseña")
            browser.find_elements_by_class_name("x-form-text")[23].send_keys("dat1234")
            logger.debug("Rellenar la confirmación de contraseña")
            browser.find_elements_by_class_name("x-form-text")[24].send_keys("dat1234")
            logger.debug("Rellenar las posiciones en tiempo real")
            logger.debug("Rellenar la fecha")
            browser.find_elements_by_class_name("x-form-text")[27].send_keys("31/12/18")
            browser.find_elements_by_class_name("x-form-text")[27].send_keys(Keys.RETURN)            
            logger.debug("Rellenar el idioma")
            browser.find_elements_by_class_name("x-form-text")[28].send_keys(unicode('es', errors='replace'))
            browser.find_elements_by_class_name("x-form-text")[28].send_keys(Keys.RETURN)
            logger.debug("Rellenar el tipo de monitorización")
            browser.find_elements_by_class_name("x-form-text")[31].send_keys("de flota")
            browser.find_elements_by_class_name("x-form-text")[31].send_keys(Keys.RETURN)
            
            '''
            buttons = browser.find_elements_by_class_name("x-btn-text");            
            i=0
            for element in buttons:
                print str(i) + ": " + element.text
                i+=1
            '''

            time.sleep(1)
            #aceptar
            browser.find_elements_by_class_name("x-btn-text")[55].click()

            time.sleep(3)

            buttons = browser.find_elements_by_class_name("x-btn-text");            

            browser.find_elements_by_class_name("x-btn-text")[52].click()
            time.sleep(1)


            browser.find_elements_by_class_name("x-btn-text")[70].click()

            buttons = browser.find_elements_by_class_name("x-btn-text");            

            time.sleep(1)
            #añadir
            browser.find_elements_by_class_name("x-btn-text")[67].click()
            time.sleep(1)
            #aceptar
            browser.find_elements_by_class_name("x-btn-text")[83].click()
            time.sleep(1)

            buttons = browser.find_elements_by_class_name("x-btn-text");            

            #si
            browser.find_elements_by_class_name("x-btn-text")[87].click()
            time.sleep(10)

            
            buttons = browser.find_elements_by_class_name("x-btn-text");            

            browser.find_elements_by_class_name("x-btn-text")[52].click()
            time.sleep(11)


            self.test_results['subtest_2'] = 0
            self.n_test_ok += 1
            logger.debug("Creación de usuario -> OK!")

            #logout            
            button = browser.find_element_by_class_name('logoutIcon')
            button.click()
            time.sleep(1)
            button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
            button[0].click()
            time.sleep(5)
            

            username = browser.find_element_by_name("user")
            password = browser.find_element_by_name("password")
            username.send_keys('0-TEST002-user')
            password.send_keys('dat1234')
            #pulsar boton de login
            button_login = browser.find_element_by_xpath("//img[contains(@src, 'transparent.png')]") 
            button_login.click()
            time.sleep(2)

            buttons = browser.find_elements_by_class_name("x-btn-text");            

            self.test_results['subtest_3'] = 0
            self.n_test_ok += 1
            logger.debug("Login con el nuevo usuario -> OK!")


            try:
                button = browser.find_element_by_link_text('0-TEST002')
                button.click()
                time.sleep(6)
                self.test_results['subtest_4'] = 0
                self.n_test_ok += 1
                logger.debug("Visualización de la flota -> OK!")

            except:
                logger.debug("Visualización de la flota -> Error")
                self.test_result_code = 2
                pass

            button = browser.find_element_by_class_name('logoutIcon')
            button.click()
            time.sleep(1)
            button = browser.find_elements_by_xpath("//*[contains(text(), 'Sí')]")
            button[0].click()
            time.sleep(2)

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

            #pulsar tab de administracion
            button = browser.find_element_by_class_name('adminIcon')
            button.click()
            time.sleep(1)
            #pulsar flotas
            button = browser.find_element_by_link_text('Operadores Web')
            button.click()
            time.sleep(1)


            grids = browser.find_elements_by_class_name("x-grid3-col");            
            try:
                i=0
                encontrado = False
                while (i<len(grids) and encontrado==False):
                    element = grids[i]
                    if (element.get_attribute("innerHTML")=='<div class="x-grid3-cell-inner x-grid3-col-0" unselectable="on">0-TEST002-user</div>'):
                        encontrado = True
                        element.click()
                    i+=1

                #eliminar operador
                browser.find_elements_by_class_name("x-btn-text")[43].click()
                time.sleep(1)

                #si
                browser.find_elements_by_class_name("x-btn-text")[41].click()
                time.sleep(10)

                #aceptar
                browser.find_elements_by_class_name("x-btn-text")[40].click()
                time.sleep(3)

                self.test_results['subtest_5'] = 0
                self.n_test_ok += 1
                logger.debug("Eliminar usuario -> OK!")
            except Exception as error:
                logger.debug("Eliminar usuario -> Error")
                self.test_result_code = 1
                pass


            try:
                #pulsar tab de administracion
                button = browser.find_element_by_class_name('adminIcon')
                button.click()
                time.sleep(1)
                #pulsar flotas
                button = browser.find_element_by_link_text('Flotas')
                button.click()
                time.sleep(1)

                grids = browser.find_elements_by_class_name("x-grid3-col");            
                i=0
                encontrado = False
                while (i<len(grids) and encontrado==False):
                    element = grids[i]
                    if (element.get_attribute("innerHTML")=='<div class="x-grid3-cell-inner x-grid3-col-0" unselectable="on">0-TEST002</div>'):
                        print "flota encontrada"
                        encontrado = True
                        element.click()
                    i+=1

                #eliminar flota
                browser.find_elements_by_class_name("x-btn-text")[51].click()
                time.sleep(3)

                #si
                browser.find_elements_by_class_name("x-btn-text")[53].click()
                time.sleep(1)

                #aceptar 
                browser.find_elements_by_class_name("x-btn-text")[52].click()
                time.sleep(1)

                self.test_results['subtest_6'] = 0
                self.n_test_ok += 1
                logger.debug("Eliminar flota -> OK!")

            except:
                logger.debug("Eliminar flota -> OK!")
                self.test_result_code = 1
                pass

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
        results_file = open(RESULTS_FILE,'w') 
        results_file.write (str(time.strftime("%d/%m/%y - %I:%M:%S")) + "," + str(self.test_result_code) + "," + str(self.n_test_ok) + "," + str(self.n_test_error) + "," + str(self.test_results['subtest_1']) + "," + str(self.test_results['subtest_2']) + "," + str(self.test_results['subtest_3']) + "," + str(self.test_results['subtest_4']) + "," + str(self.test_results['subtest_5']) + "," + str(self.test_results['subtest_6']) )
        results_file.close()

    def tearDown(self):
        logger.info("Closing Chrome browser...")
        #self.browser.close()
        logger.debug("OK!")

if __name__ == "__main__":
    unittest.main()
