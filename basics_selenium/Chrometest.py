from selenium import webdriver

class Gchrometest():
    def test(self):
        driver = webdriver.Chrome()
        driver.get('http://google.com')

gc=Gchrometest()
gc.test()