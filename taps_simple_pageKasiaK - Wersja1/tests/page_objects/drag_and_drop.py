from time import sleep
from tests.helpers.support_functions import *
from selenium.webdriver import ActionChains


drag_tap = 'draganddrop-header'
drag_content = 'draganddrop-content'
rectangle_positionA = 'column-a'
rectangle_positionB = 'column-b'


def click_draganddrop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_tap)
    elem.click()

def draganddrop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, drag_content)
    return elem.is_displayed()


def check_drag_and_drop(driver_instance):
  driver_instance.implicitly_wait(10)
  driver_instance.get('http://simpletestsite.fabrykatestow.pl/')

  with open('C:/Users/kasia/Documents/dnd.js', 'r') as js_file:
    line = js_file.readline()
    script = ''
    while line:
      script += line
      line = js_file.readline()
  driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
  return True


