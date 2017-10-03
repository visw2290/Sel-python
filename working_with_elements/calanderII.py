from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalanderII():
    def test_calander_II(self):
        url = 'https://www.expedia.co.in'
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)
        flight_tab = driver.find_element(By.ID,'tab-flight-tab').click()
        flight_departing = driver.find_element(By.ID,'flight-departing')
        flight_departing.click()
        flight_month = driver.find_element(By.XPATH,"//div[@class='datepicker-cal-month'][position()=1]")
        flight_dates = flight_month.find_elements(By.TAG_NAME,'td')

        for dates in flight_dates:
            if dates.text == '28':
                dates.click()
                break
cII = CalanderII()
cII.test_calander_II()