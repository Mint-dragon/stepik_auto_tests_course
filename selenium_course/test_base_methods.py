from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def test_find_element_by_id():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element(By.ID, "submit_button")
    return button


def test_lesson6_step4():
    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(60)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_lesson6_step5_find_link():
    
    link = "http://suninjuly.github.io/find_link_text"
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
        link.click()
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()

def test_lesson6_step6_find_elements():
    
    link="http://suninjuly.github.io/huge_form.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_elements(By.TAG_NAME, "input")
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()

def test_lesson6_step7_find_by_xpath():
    link = "http://suninjuly.github.io/find_xpath_form"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "//*[@type='submit']")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(60)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_lesson6_step8_unique_selector():
    try: 
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        elements = browser.find_elements(By.CSS_SELECTOR, "input[required]")
        for element in elements:
            element.send_keys("value")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        

