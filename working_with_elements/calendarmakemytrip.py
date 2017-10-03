from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarMMT():
    def test_calendar_MMT(self):
        url = 'https://www.makemytrip.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)
        depart_date = driver.find_element(By.ID,'hp-widget__depart')
        depart_date.click()
        month_select = driver.find_element(By.XPATH,"//div[@id = 'js-filterOptins']/div/div[3]/div/div[1]")
        date_select = month_select.find_elements(By.TAG_NAME,'a')
        for date in date_select:
            if date.text == '30':
                date.click()
                break
        time.sleep(3)
        driver.quit()

cmmt = CalendarMMT()
cmmt.test_calendar_MMT()