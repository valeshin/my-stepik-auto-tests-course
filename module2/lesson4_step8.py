from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button_book = browser.find_element_by_id('book')
    button_book.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(y)
    submit_button_end = browser.find_element_by_css_selector('.btn[type="submit"]')
    submit_button_end.click()

finally:
    time.sleep(10)
    browser.quit()
