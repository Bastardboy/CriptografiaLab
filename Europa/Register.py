import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

#/usr/local/bin/chromedriver para ejecutarlo
driver_path = '/usr/local/bin/chromedriver'

def login():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blcking')

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    #Iniciar interfaz 
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://www.micasillaeuropea.com/#registrate-o-ingresa')
    time.sleep(5)
    mail = driver.find_element_by_name('email')
    mail.clear()
    time.sleep(1)
    mail.send_keys('kexekeb899@bunlets.com')
    pwd = driver.find_element_by_name('password')
    pwd.clear()
    pwd.send_keys('muyseguro')
    driver.find_element_by_xpath('//*[@id="btnRegistrate"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="myModalRegistrate"]/div/div/div[3]/div/div[3]/button').click()
    time.sleep(5)

if __name__ == "__main__":
    login()