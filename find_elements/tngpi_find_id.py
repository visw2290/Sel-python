from selenium import webdriver

class tngID():
    def test_tng_id(self):
        driver = webdriver.Firefox()
        driver.get('http://tngpi.cisco.com/general_usage.html')
        tng_element = driver.find_element_by_partial_link_text('user config')
        tng_element.click()
        if tng_element:
            print('Found a name in tng page %s' %(tng_element))
tl = tngID()
tl.test_tng_id()