from selenium import webdriver

class practice_1():
    def test_xpath_practice(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_value = driver.find_element_by_xpath("//table[@id='product']/tbody/tr[3]/td[2]/following-sibling::td")
        print(ele_value)

pra1 = practice_1()
pra1.test_xpath_practice()

