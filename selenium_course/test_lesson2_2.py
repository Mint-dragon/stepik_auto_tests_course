from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def test_lesson2_switch_to_alert():

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/alert_accept.html")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        browser.switch_to.alert.accept()
        
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        browser.find_element(By.ID, "answer").send_keys(y)

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        print(browser.switch_to.alert.text)

    finally:
        time.sleep(5)
        browser.quit()
        

def test_lesson2_switch_to_window():

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/redirect_accept.html")

        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

              
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        browser.find_element(By.ID, "answer").send_keys(y)

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        print(browser.switch_to.alert.text.split(': ')[-1])

    finally:
        time.sleep(5)
        browser.quit()


def test_lesson2_4():

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/cats.html")

        browser.find_element(By.ID, "button")
        
    finally:
        time.sleep(5)
        browser.quit()



def test_implicitly_wait():

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        
        browser.find_element(By.ID, "book").click()

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        print(browser.switch_to.alert.text.split(': ')[-1])
        

    finally:
        time.sleep(5)
        browser.quit()


        
        
