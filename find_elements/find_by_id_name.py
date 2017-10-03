from selenium import webdriver

class Felements():
    def test_id_name(self):
        url = 'http://10.78.239.69'
        driver = webdriver.Firefox()
        driver.get(url)
        element_id = driver.find_element_by_id('username')
        if element_id:
            print('Hoorah found ID')
        element_name = driver.find_element_by_name('password')
        if element_name:
            print('Hoorah found name')
fe= Felements()
fe.test_id_name()
