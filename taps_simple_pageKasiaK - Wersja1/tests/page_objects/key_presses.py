from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys
from time import sleep

"""driver_instance = webdriver.Chrome('C:/Users/kasia/PycharmProjects/taps_simple_page/chromedriver.exe')
page_url = 'http://simpletestsite.fabrykatestow.pl'
driver_instance.get(page_url)
driver_instance.maximize_window()
"""


key_presses_tab = 'keypresses-header'
key_presses_content = 'keypresses-content'
field_input = 'target'
key_press_target = 'keyPressResult'




def click_key_presses_tab(driver_instance):
    elem = driver_instance.find_element_by_id(key_presses_tab)
    elem.click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, key_presses_content)
    return elem.is_displayed()

def key_presses_correct_value(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, field_input, 5)
    elem = driver_instance.find_element_by_id(field_input)
    elem_p = driver_instance.find_element_by_id(key_press_target)
    elem.send_keys("K")
    value = "K"
    sleep(3)
    if value == (elem_p.text[13:]):
        return True
    else:
        return False


def key_presses_Enter(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, field_input, 5)
    elem = driver_instance.find_element_by_id(field_input)
    elem.send_keys(Keys.ENTER)
    sleep(3)
    print(elem.get_attribute("value"))
    if value == (elem.get_attribute("value")):
        return True
    else:
        return False



"""
elem = driver_instance.find_element_by_id(key_presses_tab)
elem.click()
wait_for_visibility_of_element_id(driver_instance, field_input, 5)
elem1 = driver_instance.find_element_by_id(field_input)
elem_p = driver_instance.find_element_by_id(key_press_target)
elem1.send_keys("K")
sleep(5)
value = elem_p.text
value = "K"
sleep(3)
print("Wprowadzileś znak: " + value[12:])
driver_instance.quit()
"""

