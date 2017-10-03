from selenium import webdriver

class XpathCe():
    def test_xpath_CE(self):
        url = 'https://10.78.239.67'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_xpath_CE_login = driver.find_element_by_xpath("//input[@id='username']")
        if ele_xpath_CE_login:
            print('Found Xpath 1 for login')
        ele_xpath_CE_login_2 = driver.find_element_by_xpath("//div[@id='root']//div/input[@id='username']")
        if ele_xpath_CE_login_2:
            print('Found Xpath2 for login')
        ele_xpath_CE_password = driver.find_element_by_xpath(".//div[@id='root']//div/input[@name = 'password']")
        if ele_xpath_CE_password:
            print('Found Xpath1 for password')
        ele_xpath_CE_password_2 = driver.find_element_by_xpath(".//input[@name='password']")
        if ele_xpath_CE_password_2:
            print('Found Xpath2 for password')
xc= XpathCe()
xc.test_xpath_CE()
