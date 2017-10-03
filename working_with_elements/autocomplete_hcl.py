from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class HclAutoComplete():
    def test_hcl_autocomplete(self):
        url = 'https://www.myhcl.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(4)
        login_id = driver.find_element_by_id('txtUserID')
        login_id.send_keys('sw_viswanathan')
        pwd = driver.find_element_by_id('txtPassword')
        pwd.send_keys('sdbcisco.9022')
        domain = driver.find_element_by_id('ddlDomain')
        svalue = Select(domain)
        svalue.select_by_value('HCLTECH')
        submit_btn = driver.find_element_by_id('btnSubmit')
        submit_btn.click()
        search_box = driver.find_element_by_id('txtSearch')
        search_box.send_keys('itime')
        time.sleep(2)
        autocomplete_item = driver.find_element_by_xpath("//ul[@id='ui-id-1']//a[contains(text(),'iTime (Time Sheet Management System)')]")
        autocomplete_item.click()
        time.sleep(4)
        driver.quit()

hac = HclAutoComplete()
hac.test_hcl_autocomplete()