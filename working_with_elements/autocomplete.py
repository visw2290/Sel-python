from selenium import webdriver
import time
class AutoComplete():
    def test_auto_complete(self):
        url = 'https://www.southwestairlines.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)
        depart_field = driver.find_element_by_id('air-city-departure')
        depart_field.send_keys('Bos')
        time.sleep(2)
        autoclick = driver.find_element_by_xpath("//ul[@id = 'air-city-departure-menu']//li[contains(text(),'Boston Logan, MA - ')]")
        autoclick.click()
        time.sleep(3)
        driver.quit()

ac = AutoComplete()
ac.test_auto_complete()
