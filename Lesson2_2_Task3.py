from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)
    
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ivan@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'File.txt')           # добавляем к этому пути имя файла 
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)    
	# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # ждем загрузки страницы
    time.sleep(1)
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	