from selenium import webdriver

class trailXpath():
    def test_xpath_trial(self):
        url = 'https://letskodeit.teachable.com'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_xpath_trial = driver.find_element_by_xpath("//a[@class='navbar-link fedora-navbar-link']")
        if ele_xpath_trial:
            print('Found the login element using Xpath')
tx = trailXpath()
tx.test_xpath_trial()