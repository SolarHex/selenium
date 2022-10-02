from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path='C:\\Users\\roman\\OneDrive\\Рабочий стол\\sele-ni-um\\chromedriver\\chromedriver.exe',
    options=option
)

try:
    driver.get('https://vk.com/')
    time.sleep(3)
    
    login = driver.find_element_by_id('index_email')
    login.send_keys('89993953225')
    time.sleep(2)
    pasw = driver.find_element_by_id('index_pass')
    pasw.send_keys('31415926535romka')
    time.sleep(2)
    pasw.send_keys(Keys.ENTER)
    time.sleep(2)
    messages = driver.find_element_by_id('l_msg').click()
    time.sleep(2)
    g = driver.find_element_by_xpath("//li[@data-list-id='-91050183']").click()
    time.sleep(2)
    g1 = driver.find_element_by_id('im_editable0')
    g1.send_keys('REVOLULIZE')
    g1.send_keys(Keys.ENTER)
    time.sleep(2)
    messages = driver.find_element_by_id('l_msg').click()
    time.sleep(2)
    
    pin = driver.find_element_by_xpath("//li[@data-list-id='345555726']").click()
    pin = driver.find_element_by_id('im_editable0')
    pin.send_keys('Hello! =)')
    time.sleep(2)
    

except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()