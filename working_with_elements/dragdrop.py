from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class DragAndDrop():
    def test_dragdrop(self):
        url = 'http://jqueryui.com/droppable'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        #drag and drop is in iframe. so move to iframe
        driver.switch_to.frame(0)

        fromelement = driver.find_element_by_id('draggable')
        toelement = driver.find_element_by_id('droppable')

        try:
            actions = ActionChains(driver)
            #actions.drag_and_drop(fromelement,toelement).perform()
            #conventional way
            actions.click_and_hold(fromelement).move_to_element(toelement).release().perform()
            time.sleep(2)
            print('Drag and drop completed successfully')
        except:
            print('Drag and drop did not succeed')
        finally:
            driver.quit()

dad = DragAndDrop()
dad.test_dragdrop()