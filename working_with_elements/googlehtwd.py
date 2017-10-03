from selenium import webdriver
import time

class GoogleHtWd():
    def test_height_width_gle(self):
        url = 'https://www.google.com'
        driver = webdriver.Firefox()
        driver.get(url)
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height = "+ str(height))
        print("Width = "+ str(width))
        driver.quit()
ghw = GoogleHtWd()
ghw.test_height_width_gle()