import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_field = browser.find_element_by_css_selector('[name="firstname"]')
    first_name_field.send_keys('Elena')
    last_name_field = browser.find_element_by_css_selector('[name="lastname"]')
    last_name_field.send_keys('Golovach')
    email_field = browser.find_element_by_css_selector('[name="email"]')
    email_field.send_keys('nagibator777@mail.ru')
    upload_field = browser.find_element_by_id('file')
    upload_field.send_keys(file_path)
    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()

finally:
    time.sleep()
    browser.quit()
