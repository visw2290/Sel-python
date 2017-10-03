from selenium import webdriver
import time

class IsSelected():
    def test_is_selected(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        bmwradioBtn = driver.find_element_by_id('bmwradio')
        bmwradioBtn.click()
        time.sleep(2)
        benzradioBtn = driver.find_element_by_id('benzradio')
        benzradioBtn.click()
        time.sleep(2)
        bmwcheckBox = driver.find_element_by_id('bmwcheck')
        bmwcheckBox.click()
        time.sleep(2)
        hondacheckBox = driver.find_element_by_id('hondacheck')
        hondacheckBox.click()
        time.sleep(2)
        print('Is BMW radio button selected?' + str(bmwradioBtn.is_selected()))
        print('Is BENZ radio button selected?' + str(benzradioBtn.is_selected()))
        print('Is BMW checkBox selected?' + str(bmwcheckBox.is_selected()))
        print('Is Honda checkbox selected?' + str(hondacheckBox.is_selected()))
        driver.quit()
ss = IsSelected()
ss.test_is_selected()
