from selenium import webdriver

class XpathContains():
    def test_xpath_contains(self):
        url = 'https://letskodeit.teachable.com'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_xpath_contains = driver.find_element_by_xpath("//div[@id='navbar']//a[contains(@class,'navbar-link') and contains(@href,'sign_in')]")
        if ele_xpath_contains:
            print('Found Xpath using contains')
xc=XpathContains()
xc.test_xpath_contains()