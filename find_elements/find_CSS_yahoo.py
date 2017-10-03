from selenium import webdriver

class CSSYahoo():
    def test_CSS_Yahoo(self):
        url = 'https://yahoo.com'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_search_yahoo = driver.find_element_by_css_selector('#uh-search-box')
        if ele_search_yahoo:
            print('Found It by using CSS ID')

csy=CSSYahoo()
csy.test_CSS_Yahoo()