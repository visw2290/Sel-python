from selenium import webdriver
import time

class imWait():
    def test_implicitWait(self):
        url = 'https://letskodeit.teachable.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        login = driver.find_element_by_xpath("//div[@id = 'navbar']//a[contains(text(),'Login')]")
        login.click()
        username = driver.find_element_by_css_selector("input#user_email")
        username.send_keys('viswa')
        password = driver.find_element_by_xpath("//input[@id = 'user_password']")
        password.send_keys('12345')
        time.sleep(3)
        driver.quit()
iw = imWait()
iw.test_implicitWait()