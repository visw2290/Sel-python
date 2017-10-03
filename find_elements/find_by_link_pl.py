from selenium import webdriver

class Flink():
    def test_link_pl(self):
        url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(url)
        element_link = driver.find_element_by_link_text('Login')
        if element_link:
            print('Hoorah, Found element by link')
        element_plink = driver.find_element_by_partial_link_text('Prac')
        if element_plink:
            print('Hoorah, Fount partial elemment by partial link')

fl =Flink()
fl.test_link_pl()