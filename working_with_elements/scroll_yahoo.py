from selenium import webdriver
import time

class Scrollyahoo():
    def test_scroll_yahoo(self):
        url = 'https://yahoo.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0,2000);")

        driver.execute_script("window.scrollBy(0,-2000);")

        element = driver.find_element_by_xpath("//h2[contains(text(),'MMA Bangalore, Karnataka')]")
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        driver.execute_script("window.scrollBy(0,-250);")
        time.sleep(4)

        driver.execute_script("window.scrollBy(0,-2000);")
        location = element.location_once_scrolled_into_view
        print('Location = ' + str(location))
        time.sleep(2)

        driver.quit()

sy = Scrollyahoo()
sy.test_scroll_yahoo()