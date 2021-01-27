from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView();", answer_field)
    answer_field.send_keys(y)
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()
    robot_radiobutton = browser.find_element_by_id("robotsRule")
    robot_radiobutton.click()
    submit_button = browser.find_element_by_css_selector('.btn[type="submit"]')
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()

