from selenium import webdriver

class IsEnabled():
    def test_is_selected(self):
        url = 'https://google.com'
        driver = webdriver.Firefox()
        driver.get(url)
        driver.implicitly_wait(10)
        ele_search = driver.find_element_by_id('lst-ib')
        if ele_search.is_enabled():
            ele_search.send_keys('man utd')
            print('Script executed')
            driver.quit()
        else:
            print('Script not executed as locator is not enabled')
            driver.quit()

ie = IsEnabled()
ie.test_is_selected()