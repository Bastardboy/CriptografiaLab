import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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
    driver.get('https://www.entrejuegos.cl/iniciar-sesion?back=my-account')
    time.sleep(5)
    mail = driver.find_element_by_name('email')
    mail.clear()
    time.sleep(1)
    mail.send_keys('tegowo4080@dufeed.com')
    pwd = driver.find_element_by_name('password')
    pwd.clear()
    pwd.send_keys('muyseguro')
    driver.find_element_by_id("submit-login").submit()
    time.sleep(5)
    driver.quit()