link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_available_button(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector(".btn-add-to-basket"), "Couldn't find button"