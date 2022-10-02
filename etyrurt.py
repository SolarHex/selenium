import time
from selenium import webdriver




option = webdriver.ChromeOptions()
#option.add_argument(f"")
driver = webdriver.Chrome(
    executable_path='C:\\Users\\roman\\OneDrive\\Рабочий стол\\sele-ni-um\\chromedriver\\chromedriver.exe',
    options=option
    )


try:
    driver.get('')
    driver.create_web_element()
   
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()