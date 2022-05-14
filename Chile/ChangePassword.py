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
    email = driver.find_element_by_name('email')
    email.clear()
    time.sleep(1)
    email.send_keys('tegowo4080@dufeed.com')
    pswd = driver.find_element_by_name("password")
    pswd.clear()
    pswd.send_keys('muyseguro')
    driver.find_element_by_id("submit-login").submit()
    time.sleep(5)

    #Pasamos al perfil
    driver.get('https://www.entrejuegos.cl/datos-personales')
    time.sleep(5)
    newpswd = driver.find_element_by_name('password')
    newpswd.clear()
    newpswd.send_keys('muyseguro')
    newpswd2 = driver.find_element_by_name('new_password')
    newpswd2.clear()
    newpswd2.send_keys('muyseguro4')
    time.sleep(5)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="customer-form"]/footer/button').click()
    time.sleep(5)
    driver.quit()