#LIBRARIES
import string, random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#/usr/local/bin/chromedriver
driver_path = '/usr/local/bin/chromedriver'

if __name__ == "__main__":
    #Variables
    letters = string.ascii_letters
    numeros = string.digits
    Arabes = "ء آ أ ؤ ئ ا ب ة ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ل م ن ه و ي ً ٌ ٍ َ ُ ِ ّ ْ ٔ ٰ ټ پ ځ څ چ ډ ړ ږ ژ ښ ک ګ گ ڼ ی ۍ ې ﭖ ﭗ ﭘ ﭙ ﭺ ﭻ ﭼ ﭽ ﮊ ﮋ ﮎ ﮏ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﯤ ﯥ ﯦ ﯧ ﯼ ﯽ ﯾ ﯿ ﺀ ﺍ ﺎ ﺏ ﺐ ﺑ ﺒ ﺓ ﺔ ﺕ ﺖ ﺗ ﺘ ﺙ ﺚ ﺛ ﺜ ﺝ ﺞ ﺟ ﺠ ﺡ ﺢ ﺣ ﺤ ﺥ ﺦ ﺧ ﺨ ﺩ ﺪ ﺫ ﺬ ﺭ ﺮ ﺯ ﺰ ﺱ ﺲ ﺳ ﺴ ﺵ ﺶ ﺷ ﺸ ﺹ ﺺ ﺻ ﺼ ﺽ ﺾ ﺿ ﻀ ﻁ ﻂ ﻃ ﻄ ﻅ ﻆ ﻇ ﻈ ﻉ ﻊ ﻋ ﻌ ﻍ ﻎ ﻏ ﻐ ﻑ ﻒ ﻓ ﻔ ﻕ ﻖ ﻗ ﻘ ﻝ ﻞ ﻟ ﻠ ﻡ ﻢ ﻣ ﻤ ﻥ ﻦ ﻧ ﻨ ﻩ ﻪ ﻫ ﻬ ﻭ ﻮ ﻱ ﻲ ﻳ ﻴ"
    subsup = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    normal = "♫☼►◄↕‼¶§▬↨↑↓→∟↔▲▼0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
    cadena = normal + subsup + Arabes
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
    for i in range(100):
        email = driver.find_element_by_name('email')
        email.clear()
        time.sleep(1)
        email.send_keys('rofol18036@hbehs.com')
        pwd = driver.find_element_by_name('password')
        pwd.clear()
        newText = ''.join(random.choice(cadena) for j in range(random.randrange(5,70)))
        pwd.send_keys(newText)
        print('password: '+ newText)
        driver.find_element_by_id("submit-login").click()
        time.sleep(2)

    driver.close()


#1. largo minimo 5, maximo 70
#2. Sí lo restringe pidiendo una contraseña de largo mínimo y cuando pasa de 70 caracteres este
#tira un mensaje de error

#4. Sí, se transmite por texto plano, network -> inicio de sesion -> Payload (Contraseña plana)
#El correo registrado
#5. Se transmite por POST
#6. Solicita el correo para hacer efectiva la recuperación de contraseña
#7. El usuario reinicia la antigua por una nueva