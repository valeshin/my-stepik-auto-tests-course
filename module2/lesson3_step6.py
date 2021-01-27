from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
link_stepic = "https://stepik.org/"
link_step6 = "https://stepik.org/lesson/184253/step/6?unit=158843"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit_button_start = browser.find_element_by_css_selector('.btn.trollface')
    submit_button_start.click()
    window_answer = browser.window_handles[1]
    browser.switch_to.window(window_answer)

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
    enter_button = browser.find_element_by_class_name('navbar__auth_login')
    enter_button.click()
    time.sleep(5)

    login_field = browser.find_element_by_id('id_login_email')
    login_field.send_keys('v.aleshin92@gmail.com')
    password_field = browser.find_element_by_id('id_login_password')
    password_field.send_keys('norelav359')
    login_button = browser.find_element_by_css_selector('.sign-form__btn.button_with-loader')
    login_button.click()
    time.sleep(5)
    browser.get(link_step6)
    time.sleep(5)
    text_area = browser.find_element_by_class_name('textarea')
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_area)
    text_area.send_keys(answer_lesson)
    send_button = browser.find_element_by_class_name('submit-submission')
    browser.execute_script("return arguments[0].scrollIntoView(true);", send_button)
    send_button.click()

finally:
    time.sleep(10)
    browser.quit()