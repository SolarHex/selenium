from selenium import webdriver
from selenium.webdriver.common import keys
import time
import pyautogui

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path='C:\\Users\\roman\\OneDrive\\Рабочий стол\\sele-ni-um\\chromedriver\\chromedriver.exe',
    options=option
)

try:
    driver.get('https://igroutka.ru/igry-klikery/21006-kuki-kliker.html')
    time.sleep(1)
    
    cookie = driver.find_element_by_id('bigCookie').click()
    time.sleep(10)
    
    
    
except Exception as ex:
    print(ex)
finally:
    driver.quit()
    driver.close()