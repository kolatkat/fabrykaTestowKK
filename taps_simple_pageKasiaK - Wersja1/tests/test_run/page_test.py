import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, info_page, add_remove_page, basicauth_page, checkboxes_page, data_picker_page, drag_and_drop, dropdown_page, form_page, hovers_page, inputs_page, key_presses, users_page, status_code_page, respons_requests, iFrame_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/path/taps_simple_pageKasiaK - Wersja1/chromedriver.exe')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibilty(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_datapicker_visibilty(self):
        data_picker_page.click_datapicker_tab(self.driver)
        self.assertTrue(data_picker_page.datapicker_content_visible(self.driver))

    def test11_datapicker_correct_input(self):
        data_picker_page.click_datapicker_tab(self.driver)
        self.assertTrue(data_picker_page.send_correct_keys_to_input(self.driver))

    def test12_datapicker_inputs_incorrect_input(self):
        data_picker_page.click_datapicker_tab(self.driver)
        self.assertTrue(data_picker_page.send_incorrect_keys_to_input(self.driver))

    def test13_basicauth_visibility(self):
        basicauth_page.click_basicauth_tab(self.driver)
        self.assertTrue(basicauth_page.basicauth_content_visible(self.driver))

    def test14_basicauth_correct_user(self):
        basicauth_page.click_basicauth_tab(self.driver)
        basicauth_page.basicauth_correct_login(self.driver)
        self.assertTrue(info_page.info_displayed(self.driver))

    def test15_basicauth_incorrect_user(self):
        basicauth_page.click_basicauth_tab(self.driver)
        basicauth_page.basic_incorrect_login(self.driver)
        self.assertTrue(info_page.info_invalid_credentials(self.driver))

    def test16_form_visibility(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))

    def test17_form_fields_fielled(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_fields_fielled(self.driver))

    def test18_form_field_firsName_unfiield(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_field_first_name_unfielled(self.driver))

    def test19_key_presses_visibility(self):
        key_presses.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses.key_presses_content_visible(self.driver))

    def test20_key_presses_value(self):
        key_presses.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses.key_presses_correct_value(self.driver))

    def test21_key_special_presses(self):
        key_presses.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses.key_presses_Enter(self.driver))

    def test22_draganddrop_presses_visibility(self):
        drag_and_drop.click_draganddrop_tab(self.driver)
        self.assertTrue(drag_and_drop.draganddrop_content_visible(self.driver))

    def test23_draganddrop_chanche_position(self):
        drag_and_drop.click_draganddrop_tab(self.driver)
        drag_and_drop.draganddrop_content_visible(self.driver)
        self.assertTrue(drag_and_drop.check_drag_and_drop(self.driver))

    def test24_status_visibility(self):
        status_code_page.click_status_tab(self.driver)
        self.assertTrue(status_code_page.status_content_visible(self.driver))

    def test25_statusCode_200(self):
        status_code_page.click_status_tab(self.driver)
        status_code_page.status_200_clicked(self.driver)
        self.assertTrue(respons_requests.status_code_200(self.driver))

    def test26_statusCode_305(self):
        status_code_page.click_status_tab(self.driver)
        status_code_page.status_305_clicked(self.driver)
        self.assertTrue(respons_requests.status_code_305(self.driver))

    def test27_statusCode_404(self):
        status_code_page.click_status_tab(self.driver)
        status_code_page.status_404_clicked(self.driver)
        self.assertTrue(respons_requests.status_code_404(self.driver))

    def test28_statusCode_500(self):
        status_code_page.click_status_tab(self.driver)
        status_code_page.status_500_clicked(self.driver)
        self.assertTrue(respons_requests.status_code_500(self.driver))

    def test29_iFrame_visibility(self):
        iFrame_page.click_iframe_tab(self.driver)
        self.assertTrue(iFrame_page.iframe_content_visible(self.driver))

    def test30_iFrame_button1_clicked(self):
        iFrame_page.click_iframe_tab(self.driver)
        self.assertTrue(iFrame_page.button1_is_cliked(self.driver))

    def test31_iFrame_button2_clicked(self):
        iFrame_page.click_iframe_tab(self.driver)
        self.assertTrue(iFrame_page.button2_is_cliked(self.driver))