from tests.helpers.support_functions import *

return_button = 'retrun button'
login_message = 'loginFormMessage'

def info_displayed(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, return_button)
    return  elem.is_displayed()


def info_invalid_credentials(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, login_message)
    return elem.is_displayed()