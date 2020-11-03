from tests.helpers.support_functions import *


datapicker_tap = 'datepicker-header'
datapicker_content = 'datepicker-content'
input = '//*[@id="start"]'
button = 'reset-button'



def click_datapicker_tab(driver_instance):
    elem = driver_instance.find_element_by_id(datapicker_tap)
    elem.click()


def datapicker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, datapicker_content)
    return elem.is_displayed()


def send_correct_keys_to_input(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, input, time_to_wait=1)
    elem = driver_instance.find_element_by_xpath(input)
    value = '2020-07-22'
    print(elem.get_attribute("value"))
    if value == (elem.get_attribute("value")):
       return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, input, time_to_wait=1)
    elem = driver_instance.find_element_by_xpath(input)
    elem.send_keys('abcd')
    value = 'abc'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True

"""
def click_reset_button(driver_instance):
    elem = driver_instance.find_element_by_css_selector("button[id='reset-button']")
    elem.click()
    sleep(5)


def datapiker_reset_input(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, button, time_to_wait=1)
    elem_button = driver_instance.find_element_by_id(button)
    elem_button.click()
    elem_input = driver_instance.find_element_by_xpath(input)
    value = 'dd.mm.rrrr'
    sleep(5)
    print(elem_input.get_attribute("value"))
    if value == (elem_input.get_attribute("value")):
       return True
    else:
        return False
"""

"""
to dopisać do wszystkich testów po poprawie


    def test13_datapicker_button(self):
        data_picker_page.click_datapicker_tab(self.driver)
        self.assertTrue(data_picker_page.datapiker_reset_input(self.driver))

    def test14_datapiker_button_click(self):
        data_picker_page.click_datapicker_tab(self.driver)
        data_picker_page.click_reset_button(self.driver)
"""