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
    log.send_keys('####@gmail.com')
    time.sleep(1)
    psw = driver.find_element_by_name('password')
    psw.send_keys('#####')
    time.sleep(1)
    enter = driver.find_element_by_class_name('qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB')
    enter.click()
    time.sleep(3)

    #while True:
    name = driver.get('https://www.instagram.com/1lisssy/')
    time.sleep(2)  
        
    like = driver.find_element_by_class_name('v1Nh3.kIKUG._bz0w')
    like.click()
    time.sleep(2)
    
    while True:
        
        like1 = driver.find_element_by_class_name('fr66n')
        like1.click()
        time.sleep(2)
        
        photo = driver.find_element_by_class_name('l8mY4.feth3')
        photo.click()
        time.sleep(2)
        
        
except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()