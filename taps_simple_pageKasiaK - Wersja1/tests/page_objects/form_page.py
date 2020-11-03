from selenium.webdriver.support import wait

from tests.helpers.support_functions import *
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.remote.switch_to import SwitchTo
from time import sleep


form_tab = 'form-header'
form_content = 'form-content'
first_name = 'fname'
last_name = 'lname'
submit_button = 'formSubmitButton'



def click_form_tab(driver_instance):
    elem = driver_instance.find_element_by_id(form_tab)
    elem.click()


def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, form_content)
    return elem.is_displayed()


def form_fields_fielled(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, first_name, 5)
    elem_user_name = driver_instance.find_element_by_id(first_name)
    elem_user_name.send_keys('Kate')
    elem_last_name = driver_instance.find_element_by_id(last_name)
    elem_last_name.send_keys('admin')
    elem_submit_button = driver_instance.find_element_by_id(submit_button)
    elem_submit_button.click()
    alert = Alert(driver_instance)
    value = "success"
    if value == alert.text:
        return True
    else:
        return False


def form_field_first_name_unfielled(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, first_name, 5)
    elem_last_name = driver_instance.find_element_by_id(last_name)
    elem_last_name.send_keys('admin')
    elem_submit_button = driver_instance.find_element_by_id(submit_button)
    elem_submit_button.click()
    attr = driver_instance.switch_to.active_element.get_attribute("text")
    value = "Wypełnij to pole."
    if value == attr:
        return True
    else:
        return False




