import time
from selenium import webdriver

class practiceAirbnb():
    def test_airbnb(self):
        url = 'https://airbnb.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        ele_place = driver.find_element_by_id('GeocompleteController-via-SearchBarLarge-via-HeroController')
        ele_place.send_keys('Chennai')
        ele_start_date = driver.find_element_by_id('startDate')
        ele_start_date.send_keys('02/10/2017')
        ele_end_date = driver.find_element_by_id('endDate')
        ele_end_date.send_keys('03/10/2017')
        submit = driver.find_element_by_xpath("//main[@id='site-content']//span[text()='Search']")
        submit.click()
        time.sleep(3)
        driver.quit()

pra = practiceAirbnb()
pra.test_airbnb()