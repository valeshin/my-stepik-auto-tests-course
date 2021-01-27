from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    x1 = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    x2 = int(num2.text)
    y = str(x1 + x2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)

    submit_button = browser.find_element_by_css_selector('.btn[type="submit"]')
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
