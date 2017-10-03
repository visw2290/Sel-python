from selenium import webdriver
import time

class findElements():
    def test_find_elements(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        radioElements = driver.find_elements_by_xpath("//input[contains(@type,'radio') and contains(@name,'cars')]")
        size_radioElements = len(radioElements)
        for radiobtn in radioElements:
            IsSelected = radiobtn.is_selected()
            if not IsSelected:
                radiobtn.click()
                time.sleep(2)
        driver.quit()
fe = findElements()
fe.test_find_elements()