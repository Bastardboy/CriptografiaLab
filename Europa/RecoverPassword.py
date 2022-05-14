from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

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
    driver.get('https://www.micasillaeuropea.com/#registrate-o-ingresa')
    time.sleep(3)
    email = driver.find_element_by_name('email')
    email.clear()
    time.sleep(1)
    email.send_keys('tegowo4080@dufeed.com')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="frmLogin"]/div[3]/div[3]/a').click()
    time.sleep(5)
    driver.switch_to.alert.accept()
    time.sleep(5)
    driver.close()