from tests.helpers.support_functions import *
import requests

status_tap = 'statuscodes-header'
status_content = 'statuscodes-content'
status_200 = '200siteAnchor'
status_305 = '305siteAnchor'
status_404 = '404siteAnchor'
status_500 = '500siteAnchor'


def click_status_tab(driver_instance):
    elem = driver_instance.find_element_by_id(status_tap)
    elem.click()

def status_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, status_content)
    return elem.is_displayed()

def status_200_clicked(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, status_200)
    elem = driver_instance.find_element_by_id(status_200)
    elem.click()

def status_305_clicked(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, status_305)
    elem = driver_instance.find_element_by_id(status_305)
    elem.click()


def status_404_clicked(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, status_404)
    elem = driver_instance.find_element_by_id(status_404)
    elem.click()

def status_500_clicked(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, status_500)
    elem = driver_instance.find_element_by_id(status_500)
    elem.click()