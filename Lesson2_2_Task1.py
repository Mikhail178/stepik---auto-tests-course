from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
    return x + y
try:
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Firefox()
    browser.get(link)    
    num1 = browser.find_element_by_id("num1")
    x = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    y = int(num2.text)    
    sum = x + y
    sumStr = str(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sumStr)
    
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
	