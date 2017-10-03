from selenium import webdriver

class BrowserInteractions():
    def test_interatcions(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        #maximize window
        driver.maximize_window()
        #open url
        driver.get(url)
        #get title
        title = driver.title
        print('The title of the page is', title)
        #get current url
        currentUrl = driver.current_url
        print('Current url is', currentUrl)
        #refresh browser window
        driver.refresh()
        print('Browser refreshed for first time')
        #refresh browser 2nd time
        driver.get(driver.current_url)
        print('Browser refreshed 2nd time')
        #open another url
        driver.get('https://google.com')
        #go one step back in broswer
        driver.back()
        #go one step forward
        driver.forward()
        #page source
        ps = driver.page_source
        #close the driver
        #driver.close()
        #quit the driver
        driver.quit()

bi = BrowserInteractions()
bi.test_interatcions()