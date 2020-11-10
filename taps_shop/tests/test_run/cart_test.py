import  unittest
from selenium import  webdriver
from taps_shop.config.test_settings import TestSettings
from taps_shop.tests.page_objects import main_page, login_page, my_account_page, cart_page

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/kasia/PycharmProjects/fabrykaTestowKK/taps_shop/chromedriver.exe')
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_add_item_to_cart(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))

    def test2_remove_item_from_cart(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.check_item_not_in_cart(self.driver))


if __name__ == '__main__':
    unittest.main()