from selenium import webdriver

class FxpathCSS():
    def test_xpath_css(self):
        url = 'http://10.78.239.69'
        driver = webdriver.Firefox()
        driver.get(url)
        element_xpath = driver.find_element_by_xpath('//*[@id=\'username\']')
        if element_xpath:
            print('Horrah, found XPath')
        element_css = driver.find_element_by_css_selector('.btn.btn-primary.do-signin.pull-right')
        if element_css:
            print('Hoorah, found CSS')

fx=FxpathCSS()
fx.test_xpath_css()
