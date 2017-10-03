from selenium import webdriver

class CssCe():
    def test_CSS_CE(self):
        url = 'https://10.78.239.67'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_CSS_login_CE = driver.find_element_by_css_selector('input#username')
        if ele_CSS_login_CE:
            print('Found CE login 1 using CSS')
        ele_CSS_login_1_CE = driver.find_element_by_css_selector("input[name$='name']")
        if ele_CSS_login_1_CE:
            print('Found CE login 2 for CSS')
        ele_CSS_password_CE = driver.find_element_by_css_selector("input[name='password']")
        if ele_CSS_password_CE:
            print('Found CE login 1 for CSS')
        ele_CSS_password_2_CE = driver.find_element_by_css_selector("input[name*='sswo']")
        if ele_CSS_password_2_CE:
            print('Found CE login 2 for CSS')
cce = CssCe()
cce.test_CSS_CE()