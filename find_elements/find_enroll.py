from selenium import webdriver

class EnrolXpath():
    def test_enroll_xpath(self):
        url = 'https://letskodeit.teachable.com'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_enroll_xpath = driver.find_element_by_xpath(".//div[@class='homepage-hero']//a[text()='Enroll now']")
        if ele_enroll_xpath:
            print('Found Xpath for enroll element')
exp = EnrolXpath()
exp.test_enroll_xpath()