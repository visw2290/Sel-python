from selenium import webdriver

class xpathCE():
    def test_CE_contains(self):
        url = 'https://10.78.239.67'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_xpath_ce_contains = driver.find_element_by_xpath("//div[@id='root']//input[contains(@id,'user')]")
        if ele_xpath_ce_contains:
            print('Found xpath for CE using contains')
xpc = xpathCE()
xpc.test_CE_contains()