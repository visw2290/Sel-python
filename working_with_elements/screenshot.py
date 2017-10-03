from selenium import webdriver
import time

class Screenshot():
    def test_screenshot(self):
        url = 'https://letskodeit.teachable.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)
        login_link = driver.find_element_by_css_selector("a[href='/sign_in']").click()
        uname = driver.find_element_by_id('user_email').send_keys('viswa@gnj.com')
        pwd = driver.find_element_by_id('user_password').send_keys('oiuyjj')
        submit_btn = driver.find_element_by_name('commit').click()

        try:
            driver.save_screenshot('c:\\adb\\selenium.png')
            print('Screenshot saved')
        except NotADirectoryError:
            print('Check the directory name given')
        finally:
            driver.quit()

ss = Screenshot()
ss.test_screenshot()