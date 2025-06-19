from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def test_lesson2_step1():
       
    try:
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/math.html")

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text #Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
        y = calc(x)

        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.ID, "robotsRule").click()
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    finally:
        time.sleep(30)
        browser.quit()



def test_get_attribute():
           
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/get_attribute.html")

        chest = browser.find_element(By.TAG_NAME, "img")
        x = chest.get_attribute("valuex")
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)



        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.ID, "robotsRule").click()
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()


    finally:
        time.sleep(10)
        browser.quit()

"""people_radio = browser.find_element(By.ID, "peopleRule")
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert people_checked is not None, "People radio is not selected by default"

        robots_radio = browser.find_element(By.ID, "robotsRule")
        robots_checked = robots_radio.get_attribute("checked")
        assert robots_checked is None, "Robots radio is not selected by default" """


def test_lesson2_step2_dropdown():
    try:
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/selects1.html")

        x_element = browser.find_element(By.ID, "num1")
        x = x_element.text
        y_element = browser.find_element(By.ID, "num2")
        y = y_element.text
        sum_number = int(x) + int(y)

        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value(str(sum_number))

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    finally:
        time.sleep(10)
        browser.quit()
        
def test_lesson2_step3_alert():
    try:
        browser = webdriver.Chrome()
        browser.get("https://SunInJuly.github.io/execute_script.html")
        button = browser.find_element(By.TAG_NAME, "button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        
    finally:
        time.sleep(10)
        browser.quit()
        

def test_lesson2_step4_execute_script():
    try:
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/execute_script.html")

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        browser.find_element(By.ID, "answer").send_keys(y)

        submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
        
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.ID, "robotsRule").click()
        submit_button.click()

    finally:
        time.sleep(10)
        browser.quit()


def test_lesson2_step5_file_upload():

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/file_input.html")

    # Заполняем текстовые поля
        elements = browser.find_elements(By.CSS_SELECTOR, "input[type=text]")
        for element in elements:
            element.send_keys("value")
        
        # Создаем файл
        file_path = os.path.abspath("test.txt")
        with open(file_path, "w") as file:
            file.write("automationbypython")

        browser.find_element(By.ID, "file").send_keys(file_path)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
           
    
    finally:
        time.sleep(10)
        browser.quit()
        os.remove(file_path) # удаляем
   

