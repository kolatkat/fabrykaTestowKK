from tests.helpers.support_functions import *


iFrame_tab = 'iframe-header'
iFrame_content = 'iframe-content'
button_first = 'simpleButton1'
button_second = 'simpleButton2'
messege = 'whichButtonIsClickedMessage'

def click_iframe_tab(driver_instance):
    elem = driver_instance.find_element_by_id(iFrame_tab)
    elem.click()


def iframe_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, iFrame_content)
    return elem.is_displayed()


def button1_is_cliked(driver_instance):
    driver_instance.switch_to.frame(0)
    elem = driver_instance.find_element_by_id(button_first)
    result = driver_instance.find_element_by_id(messege)
    elem.click()
    value = "Button 1 was clicked!"
    if (value == result.text):
        driver_instance.switch_to.default_content()
        return True
    else:
        return False


def button2_is_cliked(driver_instance):
    driver_instance.switch_to.frame(0)
    elem = driver_instance.find_element_by_id(button_second)
    result = driver_instance.find_element_by_id(messege)
    elem.click()
    value = "Button 2 was clicked!"
    if (value == result.text):
        driver_instance.switch_to.default_content()
        return True
    else:
        return False