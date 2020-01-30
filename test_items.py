import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_lang_browser(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector("#add_to_basket_form > button"))
    assert button == 1, \
    f"Need 1 buy button, but got {button}" 

