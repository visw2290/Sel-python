import time
from selenium import webdriver

class ClickSendKeys():
    def test_clicksend(self):
        url = 'https://letskodeit.teachable.com'
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        login = driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/sign_in']")
        login.click()
        username = driver.find_element_by_id('user_email')
        username.send_keys('heyyou')
        password = driver.find_element_by_id('user_password')
        password.send_keys('hello')

        time.sleep(3)

        username.clear()
        password.clear()

        time.sleep(3)

        username.send_keys('viswa')
        password.send_keys('heyuui')

csk = ClickSendKeys()
csk.test_clicksend()