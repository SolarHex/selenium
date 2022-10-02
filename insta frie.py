from selenium import webdriver
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys


option = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path='C:\\Users\\roman\\OneDrive\\Рабочий стол\\sele-ni-um\\chromedriver\\chromedriver.exe',
    options=option
)

try:
    driver.get('https://www.instagram.com/')
    time.sleep(1)
    
    log = driver.find_element_by_name('username')
    log.send_keys('i.zer1ya.i@gmail.com')
    time.sleep(2)
    psw = driver.find_element_by_name('password')
    psw.send_keys('31415926535r')
    time.sleep(2)
    enter = driver.find_element_by_class_name('qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB')
    enter.click()
    time.sleep(3)
    
    quit = driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
    quit.click()
    time.sleep(2)

    ttt = driver.find_element_by_class_name('aOOlW.bIiDR')
    ttt.click()
    time.sleep(2)

    all = driver.find_element_by_class_name('_7UhW9.PIoXz.qyrsm.KV-D4.uL8Hv')
    all.click()
    time.sleep(3)

    while True:
        frie = driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
        frie.click()
        time.sleep(1)
        
        driver.get('https://www.instagram.com/explore/people/')
        time.sleep(3)
        
        

except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()