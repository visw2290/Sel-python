from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class dropDown():
    def test_dropDown(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        ele_dropDown = driver.find_element_by_id('carselect')
        car_select = Select(ele_dropDown)
        car_select.select_by_visible_text('Benz')
        time.sleep(2)
        car_select.select_by_visible_text('Honda')
        time.sleep(2)
        driver.quit()
dd = dropDown()
dd.test_dropDown()