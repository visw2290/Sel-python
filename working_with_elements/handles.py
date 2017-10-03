from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Handles():
    def test_handles(self):
        url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(3)
    #find parent handle
        parent_handle = driver.current_window_handle
        print('Parent Handle = ' + parent_handle)
    #Select Open Window
        driver.find_element(By.ID,'openwindow').click()
    #switch to new window
        handles = driver.window_handles
        for handle in handles:
            print('Handle = ' + handle)
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print('Switched to handle = ' + handle)
                searchCourses = driver.find_element(By.ID,'search-courses')
                searchCourses.send_keys('python')
                time.sleep(2)
                driver.close()
                break
    #switch to parent handle
        driver.switch_to.window(parent_handle)
        driver.find_element(By.ID,'name').send_keys('Test is done')

hl = Handles()
hl.test_handles()