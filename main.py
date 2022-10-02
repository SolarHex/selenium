from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.webdriver.firefox import options
import random



useragent = UserAgent()
#url = 'https://www.instagram.com/'
option = webdriver.ChromeOptions()
option.add_argument(f"user-agent={useragent.random}")
driver = webdriver.Chrome(
    executable_path='C:\\Users\\roman\\OneDrive\\Рабочий стол\\sele-ni-um\\chromedriver\\chromedriver.exe',
    options=option)




try:
    driver.get(url='https://www.whatismybrowser.com/detect/what-is-my-user-agent')
    time.sleep(5)
    driver.fullscreen_window()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()