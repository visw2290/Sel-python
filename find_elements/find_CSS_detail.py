from selenium import webdriver

class findCSS():
    def test_CSS_detail(self):
        url = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_CSS = driver.find_element_by_css_selector("#carselect")
        if ele_CSS:
            print('Good Job')
fc=findCSS()
fc.test_CSS_detail()