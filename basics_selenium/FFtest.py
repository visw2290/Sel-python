from selenium import webdriver

class FirefoxTest():

    def test(self):
        # Instatiate FF browser command
        driver = webdriver.Firefox()
        # Open the URl provided
        driver.get("http://www.letskodeit.com")

ff = FirefoxTest()
ff.test()

