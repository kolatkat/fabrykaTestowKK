from tests.helpers.support_functions import *

basicauth_tap = 'basicauth-header'
basicauth_content = 'basicauth-content'
user_name = 'ba_username'
user_password = 'ba_password'
button_login = '//*[@id="content"]/button'


def click_basicauth_tab(driver_instance):
    elem = driver_instance.find_element_by_id(basicauth_tap)
    elem.click()


def basicauth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, basicauth_content)
    return elem.is_displayed()

def basicauth_correct_login(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, user_name, 5)
    elem_user_name  = driver_instance.find_element_by_id(user_name)
    elem_user_name.send_keys('admin')
    elem_user_password = driver_instance.find_element_by_id(user_password)
    elem_user_password.send_keys('admin')
    elem_login_button = driver_instance.find_element_by_xpath(button_login)
    elem_login_button.click()

def basic_incorrect_login(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, user_name, 5)
    elem_user_name = driver_instance.find_element_by_id(user_name)
    elem_user_name.send_keys('admin1')
    elem_user_password = driver_instance.find_element_by_id(user_password)
    elem_user_password.send_keys('admin1')
    elem_login_button = driver_instance.find_element_by_xpath(button_login)
    elem_login_button.click()


