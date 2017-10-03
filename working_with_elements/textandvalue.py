from selenium import webdriver
import time

class TextValue():
    def test_text_value(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        ele_text = driver.find_element_by_xpath("//a[@id='opentab']")
        ele_name_text = ele_text.text
        print('The text in the element is ' + ele_name_text)
        ele_value  = driver.find_element_by_xpath("//input[@id='name']")
        print('The value of class attribute of ele_value is ' + ele_value.get_attribute("class"))
        driver.quit()

tv = TextValue()
tv.test_text_value()