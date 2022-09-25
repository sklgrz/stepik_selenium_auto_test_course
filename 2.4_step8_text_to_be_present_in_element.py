from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math


link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(link)
    flag = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
        )
    button1 = browser.find_element(By.ID, 'book').click()

    num = browser.find_element(By.ID, 'input_value').text
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(num))
    button2 = browser.find_element(By.ID, 'solve').click()

    result = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    print(result)
    
