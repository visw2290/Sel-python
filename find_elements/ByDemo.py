from selenium import webdriver
from selenium.webdriver.common.by import By

class byCheck():
    def test_find_by(self):
        url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_id = driver.find_element(By.ID,'name')

        if ele_id:
            print('Found ID using By class')

        ele_xpath = driver.find_element(By.XPATH,".//*[@id='alertbtn']")

        if ele_xpath:
            print("Found XPATH by using By class")

        ele_linktext = driver.find_element(By.LINK_TEXT, 'Practice')

        if ele_linktext:
            print('Found Link Text using By class')

byC = byCheck()
byC.test_find_by()

