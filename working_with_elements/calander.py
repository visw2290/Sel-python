from selenium import webdriver
import time

class CalanderSelect():
    def test_calender(self):
        url = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        date_select = driver.find_element_by_xpath("//input[@id = 'package-departing-hp-package']")
        date_select.click()
        my_date = driver.find_element_by_xpath("//section[@class='package-form-fields']//button[@data-month='7' and @data-day = '26']")
        my_date.click()
        time.sleep(6)
        driver.quit()

cs = CalanderSelect()
cs.test_calender()