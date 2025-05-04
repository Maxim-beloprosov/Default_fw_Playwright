from Test.test_base import TestBase


class WebTestBase(TestBase):

    def setup_class(self):
        self.APP.browser_manager.get_browser()

    def setup_method(self):
        self.APP.web_fw_base.open_main_page()

    def teardown_method(self):
        self.APP.web_fw_base.allure_screenshot()

    def teardown_class(self):
        self.APP.browser_manager.stop_browser()


