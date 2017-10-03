import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class myhclAuth():
    def test_authentication(self):
        url = 'https://www.myhcl.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        driver.find_element_by_name('txtUserID').send_keys('sw_viswanathan')
        driver.find_element_by_name('txtPassword').send_keys('######')
        svalue = driver.find_element_by_id('ddlDomain')
        sel = Select(svalue)
        sel.select_by_value('HCLTECH')
        driver.find_element_by_id('btnSubmit').click()
        driver.find_element_by_xpath("//a[contains(text(),'HR Studio')]").click()
        driver.find_element_by_xpath("//area[@id='imap3']").click()
        driver.execute_script("window.scroll(0,1000)")
        driver.find_element_by_xpath("//a[contains(text(),'Resource Assignation System')]").click()
        time.sleep(10)
        driver.quit()

ta=myhclAuth()
ta.test_authentication()