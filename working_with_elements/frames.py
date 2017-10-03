from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class iFrames():
    def test_frames(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.execute_script("window.scrollBy(0,1000);")

        #switch to iframe in the webpage
        driver.switch_to.frame('courses-iframe')
        time.sleep(2)

        #search courses inside iframe
        courses = driver.find_element(By.ID,'search-courses')
        courses.send_keys('python')
        time.sleep(2)
        a1=driver.switch_to.alert
        a1.authenticate()

        #move to parent window again
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        driver.find_element(By.ID,'name').send_keys('Test is good')
        time.sleep(2)
        driver.quit()

ifr = iFrames()
ifr.test_frames()