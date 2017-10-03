from selenium import webdriver

class GoogleID:
    def test_google_ID(self):
        url = 'https://google.com'
        driver = webdriver.Firefox()
        driver.get(url)
        ele_gl = driver.find_element_by_id('hplogo')
        text = ele_gl.text
        if ele_gl:
            print('Hurrah!!!, Found the id name of finding lucky ' +text)
        driver.quit()


gid = GoogleID()
gid.test_google_ID()