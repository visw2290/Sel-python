from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptpop():
    def test_js_popup(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        driver.find_element(By.ID,'name').send_keys('viswa')
        driver.find_element(By.ID,'alertbtn').click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)
        driver.find_element(By.ID,'confirmbtn').click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(2)
        driver.quit()
jsp = JavaScriptpop()
jsp.test_js_popup()