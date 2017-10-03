from selenium import webdriver
import time

class WindowSize():
    def test_window_size(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get(url)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print('Height = ' + str(height))
        print('Width = '+ str(width))
        driver.quit()

ws = WindowSize()
ws.test_window_size()