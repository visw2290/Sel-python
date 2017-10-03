from selenium import webdriver
import time

class TMSJavaScript():
    def test_Tms_js(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('http://insync.cisco.com')
        alert1 = driver.switch_to.alert
        alert1.authenticate('visswami','P90hukqdou')
        time.sleep(5)

tjs = TMSJavaScript()
tjs.test_Tms_js()