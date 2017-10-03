from selenium import webdriver
import time

class JavaScript():
    def test_jscript(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)
        el = driver.find_element_by_xpath("//input[@id='name']")
        el.send_keys('viswa')
        time.sleep(3)
        driver.quit()

js = JavaScript()
js.test_jscript()

