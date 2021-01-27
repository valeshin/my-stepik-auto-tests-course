from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
link_stepic = "https://stepik.org/lesson/184253/step/4?unit=158843"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit_button_start = browser.find_element_by_css_selector('.btn[type="submit"]')
    submit_button_start.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(y)
    submit_button_end = browser.find_element_by_css_selector('.btn[type="submit"]')
    submit_button_end.click()
    alert = browser.switch_to.alert
    answer_lesson = alert.text.split(': ')[-1]
    alert.accept()
    print(answer_lesson)
    browser.get(link_stepic)
    text_area = browser.find_element_by_class_name('textarea')
    text_area.send_keys(answer_lesson)
    send_button = browser.find_element_by_class_name('submit-submission')

finally:
    time.sleep(10)
    browser.quit()
