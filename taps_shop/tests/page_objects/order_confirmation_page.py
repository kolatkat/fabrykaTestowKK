from taps_shop.tests.helpers.support_functions import *
from taps_shop.tests.page_objects import order_page
from time import sleep

article_header = 'post-8'
total_price = '/html/body/div/div[2]/div/div/main/article/div/div/div/ul/li[3]/strong/span/bdi'

def article_header_is_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, article_header)
    elem = driver_instance.find_element_by_id(article_header)
    sleep(7)
    return elem.is_displayed()

def total_price_is_correct(driver_instance, price):
    elem = driver_instance.find_element_by_xpath(total_price)
    value = elem.text
    print(value)
    if (value == price):
        return True
    else:
        return False