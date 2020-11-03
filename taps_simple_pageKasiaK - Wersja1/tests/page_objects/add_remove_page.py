from tests.helpers.support_functions import *


add_remove_elem_tab = 'addremoveelements-header'
add_remove_elem_content = 'addremoveelements-content'
new_elem = '//*[@id="addremoveelements-content"]/div/div/button'
added_element = '//*[@id="elements"]/button'


def click_and_remove_tab(driver_instance):
    elem = driver_instance.find_element_by_id(add_remove_elem_tab)
    elem.click()


def add_remove_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, add_remove_elem_content)
    return elem.is_displayed()


def add_element(driver_instance):
    elem = driver_instance.find_element_by_xpath(new_elem)
    elem.click()


def delete_element(driver_instance):
    elem = driver_instance.find_element_by_xpath(added_element)
    elem.click()
    wait_for_invisibility_of_element_xpath(driver_instance, added_element)


def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element_xpath(driver_instance, added_element)
        return True
    except NoSuchElementException:
        return False
