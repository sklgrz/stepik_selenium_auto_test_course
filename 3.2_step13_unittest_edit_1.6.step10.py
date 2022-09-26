from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest


class TestWeb(unittest.TestCase):
    def test_link1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        with webdriver.Chrome() as browser:
            browser.implicitly_wait(5)
            browser.get(link)
            
            input1 = browser.find_element(By.CLASS_NAME, 'first_block .first')
            input1.send_keys('Ivan')
            input2 = browser.find_element(By.CLASS_NAME, 'first_block .second')
            input2.send_keys('Petrov')
            input3 = browser.find_element(By.CLASS_NAME, 'first_block .third')
            input3.send_keys('ESSSSSS@mail.ru' )
            button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
            button.click()
            
            welcome_text_elt =browser.find_element(By.TAG_NAME, 'h1')
            welcome_text = welcome_text_elt.text
            
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_link2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        with webdriver.Chrome() as browser:
            browser.implicitly_wait(5)
            browser.get(link)

            input1 = browser.find_element(By.CLASS_NAME, 'first_block .first')
            input1.send_keys('Ivan')
            input2 = browser.find_element(By.CLASS_NAME, 'first_block .second')
            input2.send_keys('Petrov')
            input3 = browser.find_element(By.CLASS_NAME, 'first_block .third')
            input3.send_keys('ESSSSSS@mail.ru' )
            button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
            button.click()

            welcome_text_elt =browser.find_element(By.TAG_NAME, 'h1')
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == '__main__':
    unittest.main()
