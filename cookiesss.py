import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox import options
import pickle



option = webdriver.ChromeOptions()
#option.add_argument(f"")
driver = webdriver.Chrome(
    executable_path='C:\\Users\\roman\\OneDrive\\Рабочий стол\\sele-ni-um\\chromedriver\\chromedriver.exe',
    options=option
    )


try:
    #driver.get(url='https://vk.com/')
    #time.sleep(5)
    
    #email_input = driver.find_element_by_id('index_email')
    #email_input.clear()
    #email_input.send_keys('89993953225')
    #time.sleep(2)
    #pass_index = driver.find_element_by_id('index_pass')
    #pass_index.clear()
    #a = pass_index.send_keys('31415926535romka')
    #print(a)
#    time.sleep(2)
#    enter = driver.find_element_by_id('index_login_button').click()
 #   time.sleep(10)
  #  
   # pickle.dump(driver.get_cookies(), open('cookies','wb'))
  
    driver.get('https://vk.com/')
    time.sleep(2)
    
    for cookie in pickle.load(open('cookies','rb')):
        driver.add_cookie(cookie)
    
    time.sleep(2)
    driver.refresh()
    time.sleep(5)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()