link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_of_add_to_basket_button(browser):
    browser.get(link)
    add_to_basket_button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(add_to_basket_button) != 0, "Add to basket button is missing on the page!!!"
