import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#/usr/local/bin/chromedriver para ejecutarlo
driver_path = '/usr/local/bin/chromedriver'

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    #Iniciar interfaz
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://www.entrejuegos.cl/iniciar-sesion?create_account=1')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[1]/div[1]/label[1]/span/input').click()
    #tratamiento.clear()
    time.sleep(1)
    firstname = driver.find_element_by_name('firstname')
    firstname.clear()
    firstname.send_keys("Julian")
    lastname = driver.find_element_by_name('lastname')
    lastname.clear()
    lastname.send_keys('Alvarez')
    #provincia = driver.find_element_by_name('Provincia')
    email = driver.find_element_by_name('email')
    email.clear()
    email.send_keys('meyixon239@hhmel.com')
    pwd = driver.find_element_by_name('password')
    pwd.clear()
    pwd.send_keys('muyseguro')
    driver.find_element_by_xpath('//*[@id="customer-form"]/footer/button').click()
    time.sleep(6)
    
    driver.close()