from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class displayCheck():
    def test_display_letskode(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        ele_hidden_text = driver.find_element_by_id('displayed-text')
        print('The text box is hidden? ' + str(ele_hidden_text.is_displayed()))
        ele_hide = driver.find_element_by_id('hide-textbox')
        ele_hide.click()
        print('The text box is hidden? ' + str(ele_hidden_text.is_displayed()))
        ele_show = driver.find_element_by_id('show-textbox')
        ele_show.click()
        print('The text box is hidden? ' + str(ele_hidden_text.is_displayed()))
        driver.quit()
    def test_display_expedia(self):
        url1 = 'https://www.expedia.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url1)
        driver.implicitly_wait(5)
        ele_hidden_expedia = driver.find_element_by_id('package-1-age-select-1-hp-package')
        print('The drop down box is hidden? ' + str(ele_hidden_expedia.is_displayed()))
        ele_show_drop = driver.find_element_by_id('package-1-children-hp-package')
        select_ele_show_drop = Select(ele_show_drop)
        select_ele_show_drop.select_by_value('2')
        print('The drop down box is hidden? ' +str(ele_hidden_expedia.is_displayed()))
        driver.quit()
dc=displayCheck()
dc.test_display_letskode()
dc.test_display_expedia()
