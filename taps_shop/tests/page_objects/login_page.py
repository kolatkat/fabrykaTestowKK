from taps_shop.tests.helpers.support_functions import *
from taps_shop.tests.helpers.DataGenerator import *

username = 'username'
password = 'password'
login_button = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
random_password = 'password'
error_info = '//*[@id="content"]/div/div[1]/ul'

proper_email1 = 'cotaga1249@maillei.net'
proper_password1 = 'VRrMhK8MqFyd'

def correct_login(driver_instance):
    elem = driver_instance.find_element_by_id(username)
    elem.send_keys(proper_email1)
    elem1 = driver_instance.find_element_by_id(password)
    elem1.send_keys(proper_password1)
    elem2  = driver_instance.find_element_by_xpath(login_button)
    elem2.click()

def incorrect_login(driver_instance):
    elem = driver_instance.find_element_by_id(username)
    elem.send_keys(DataGenerator.generateWrongEmail())
    elem1 = driver_instance.find_element_by_id(password)
    elem1.send_keys(random_password)
    elem2 = driver_instance.find_element_by_xpath(login_button)
    elem2.click()
    try:
        wait_for_visibility_of_element_xpath(driver_instance, error_info)
        return  elem2.is_displayed()
    except StaleElementReferenceException:
        print('ERROR WRONG USER/PASSWORD')
        return True