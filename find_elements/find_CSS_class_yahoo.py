from selenium import webdriver

class findCssClass():
    def test_find_class_CSS(self):
        url = 'https://yahoo.com'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_class_yahoo = driver.find_element_by_css_selector("a[class^='Pos(r) D(ib) Ta(s)']")
        if ele_class_yahoo:
            print('Found using CSS class and wildcards')
fcc=findCssClass()
fcc.test_find_class_CSS()