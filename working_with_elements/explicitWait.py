from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class ExplicitDemo():
    def test_explicitDemo(self):
        url = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(.5)
        flight_select = driver.find_element_by_xpath("//button[@id = 'tab-flight-tab-hp']").click()
        flight_from = driver.find_element_by_xpath("//input[@id ='flight-origin-hp-flight']").send_keys('SFO')
        flight_to = driver.find_element_by_id('flight-destination-hp-flight').send_keys('NYC')
        flight_date = driver.find_element_by_xpath("//input[@id = 'flight-departing-hp-flight']").send_keys('10/08/2017')
        flight_return = driver.find_element_by_xpath("//input[@id = 'flight-returning-hp-flight']")
        flight_return.clear()
        flight_return.send_keys('10/19/2017')
        search_btn = driver.find_element_by_xpath("//form[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()
        wait = WebDriverWait(driver,10,poll_frequency=1,ignored_exceptions=[NoSuchElementException,
                                                                            ElementNotVisibleException,ElementNotSelectableException,StaleElementReferenceException])
        element = wait.until(EC.element_to_be_clickable((By.ID,'stopFilter_stops-0')))
        element.click()
        time.sleep(5)
        driver.quit()

ew = ExplicitDemo()
ew.test_explicitDemo()