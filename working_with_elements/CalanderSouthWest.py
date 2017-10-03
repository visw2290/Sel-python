from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalSouthWest():
    def test_calander_southwest(self):
        url = 'https://www.southwestairlines.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)
        calclick = driver.find_element(By.ID,'air-date-departure')
        calclick.click()
        calmonth = driver.find_element(By.XPATH,"//div[@class = 'calendar-1 js-calendar-1']")
        caldates = calmonth.find_elements(By.TAG_NAME,'td')

        for dates in caldates:
            if dates.text == '30':
                dates.click()
                break
        time.sleep(2)
        driver.quit()

csw = CalSouthWest()
csw.test_calander_southwest()