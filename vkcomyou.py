import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox import options
import random

option = webdriver.ChromeOptions()
#option.add_argument(f"")
driver = webdriver.Chrome(
    executable_path='C:\\Users\\roman\\OneDrive\\Рабочий стол\\sele-ni-um\\chromedriver\\chromedriver.exe',
    options=option
    )

# 3! = 6 вариантов + 2! = 2
vika_random_password = 'zig1488','zig1488A','A1488zig','zigA1488','Azig1488','1488zig','1488zigA','1488Azig'

try:
    driver.get(url='https://vk.com/')
    time.sleep(5)
    
    email_input = driver.find_element_by_id('index_email')
    email_input.clear()
    email_input.send_keys('myexnumber')
    time.sleep(2)
    pass_index = driver.find_element_by_id('index_pass')
    pass_index.clear()
    a = pass_index.send_keys(random.choice(vika_random_password))
    print(a)
    time.sleep(2)
    enter = driver.find_element_by_id('index_login_button').click()
    time.sleep(10)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()