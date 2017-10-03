from selenium import webdriver
import time

class ScrollWindow():
    def test_scroll(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(2)

        #Scroll Down
        driver.execute_script("window.scrollBy(0,2000);")
        time.sleep(3)

        #Scroll up
        driver.execute_script("window.scrollBy(0,-2000);")
        time.sleep(3)

        #move the scroll to specified element
        element = driver.find_element_by_id('mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-250);")
        time.sleep(2)

        #native way to scroll to specified element
        driver.execute_script("window.scrollBy(0,-2000);")
        location = element.location_once_scrolled_into_view
        print('location =' + str(location))
        time.sleep(2)

        driver.quit()


sw = ScrollWindow()
sw.test_scroll()