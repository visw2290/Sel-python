from selenium import webdriver

class find_starts_with_xpath():
    def test_starts_with(self):
        url = 'https://letskodeit.teachable.com'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_starts_with = driver.find_element_by_xpath("//div[@id='navbar']//a[starts-with(@class,'navbar-link')]")
        if ele_starts_with:
            print('Found Xpath using starts-with')

fsw = find_starts_with_xpath()
fsw.test_starts_with()