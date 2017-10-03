from selenium import webdriver
from selenium.webdriver.common.by import By

class findElements():
    def test_find_elements(self):
        url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(url)
        eles_class = driver.find_elements_by_class_name('inputs')
        if eles_class:
            print('The contents of eles_class is', eles_class)
        eles_tag = driver.find_elements(By.TAG_NAME,'tr')
        if eles_tag:
            print('the conetents of eles_tag is', eles_tag)
fes=findElements()
fes.test_find_elements()