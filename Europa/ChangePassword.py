import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#/usr/local/bin/chromedriver para ejecutarlo
driver_path = '/usr/local/bin/chromedriver'

def cambio():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    #Iniciar interfaz 
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://temp-mail.org/es')
    time.sleep(5)

    email = driver.find_element_by_name('email')
    email.clear()
    time.sleep(1)
    email.send_keys('kexekeb899@bunlets.com')
    pswd = driver.find_element_by_name("password")
    pswd.clear()
    pswd.send_keys('muyseguro')
    driver.find_element_by_id("submit-login").submit()
    time.sleep(5)

if __name__ == "__main__":
    #Variables
    cambio()