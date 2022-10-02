import time
from selenium import webdriver
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
    login.send_keys('herewasmyphonenumber')
    time.sleep(1)
    pasw = driver.find_element_by_id('index_pass')
    pasw.send_keys('herewasmypassport')
    time.sleep(1)
    pasw.send_keys(Keys.ENTER)
    time.sleep(1)
    
    while True:
        friends = driver.find_element_by_id('l_fr')
        friends.click()
        time.sleep(1)
        new_f = driver.find_element_by_id('ui_rmenu_find')
        new_f.click()
        time.sleep(1)
        
        addowner = driver.find_element_by_class_name('friends_find_user_add')
        addowner.click()
        time.sleep(1)
    
    
    
except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()    