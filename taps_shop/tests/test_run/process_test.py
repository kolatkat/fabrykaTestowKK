import  unittest
from selenium import  webdriver
from taps_shop.config.test_settings import TestSettings
from taps_shop.tests.page_objects import main_page, login_page, my_account_page, cart_page, order_page, order_confirmation_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/kasia/PycharmProjects/fabrykaTestowKK/taps_shop/chromedriver.exe')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_process(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        price = order_page.total_price(self.driver)
        order_page.submit_order(self.driver)
        order_confirmation_page.article_header_is_visible(self.driver)
        self.assertTrue(order_confirmation_page.total_price_is_correct(self.driver, price))



if __name__ == '__main__':
    unittest.main()