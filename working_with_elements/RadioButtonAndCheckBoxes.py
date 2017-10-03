from selenium import webdriver
import time

class radioCheck():
    def test_radio_checkbox(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(url)
        bmwRadioBtn = driver.find_element_by_id('bmwradio')
        bmwRadioBtn.click()
        time.sleep(2)
        hondaradioBtn = driver.find_element_by_id('hondaradio')
        hondaradioBtn.click()
        time.sleep(2)
        bmwcheckBox = driver.find_element_by_id('bmwcheck')
        bmwcheckBox.click()
        time.sleep(2)
        benzcheckBox = driver.find_element_by_id('benzcheck')
        benzcheckBox.click()
        time.sleep(2)
        driver.quit()
rc = radioCheck()
rc.test_radio_checkbox()