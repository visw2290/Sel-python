from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MouseHover():
    def test_mousehover(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.execute_script("window.scrollBy(0,700);")
        hoverarea = driver.find_element(By.ID,'mousehover')
        itemtoclick = "//div[@class='mouse-hover-content']//a[text()='Top']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(hoverarea).perform()
            print('Moved to the hoverarea')
            time.sleep(3)
            TopClick = driver.find_element(By.XPATH,itemtoclick)
            TopClick.click()
            time.sleep(2)
            #Actions class can also be used for clicking
            #actions.move_to_element(TopClick).click().perform()
            print('Click Top under MouseHover')
        except:
            print('Mouse Hover Test not successful')
        finally:
            driver.quit()

mh = MouseHover()
mh.test_mousehover()