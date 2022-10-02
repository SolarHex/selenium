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
    driver.get('https://vk.com/')
    time.sleep(1)
    
    login = driver.find_element_by_id('index_email')
    login.send_keys('89521143168')
    time.sleep(1)
    pasw = driver.find_element_by_id('index_pass')
    pasw.send_keys('Hhgtsz13')
    time.sleep(1)
    pasw.send_keys(Keys.ENTER)
    time.sleep(1)
    
    
    driver.get('https://vk.com/#####')
    time.sleep(2)
    
    
    
    photo = driver.find_element_by_class_name('page_square_photo.crisp_image ')
    photo.click()
    time.sleep(2)
    
    
    while True:
        like = driver.find_element_by_class_name('like_button_icon')
        like.click()
        time.sleep(3)
    
        arr = driver.find_element_by_class_name('scroll_fix_wrap.fixed.layer_wrap.pv_layer_wrap')
        arr.click()
        time.sleep(2)
    
    
    
except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()