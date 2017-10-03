from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Sliders():
    def test_slide(self):
        url = 'http://jqueryui.com/slider'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH,"//div[@id ='slider']//span")
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element,100,0).perform()
            print('Sliding successful')
            time.sleep(3)
        except:
            print('Sliding not successful')
        finally:
            driver.quit()
sl = Sliders()
sl.test_slide()

