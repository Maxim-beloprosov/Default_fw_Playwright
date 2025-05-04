from Test.web_tests.web_test_base import WebTestBase
import allure


@allure.story('Google test')
class TestGoogle(WebTestBase):

    @allure.title('Search in Google and next actions')
    def test_search_in_google_and_next_actions(self):
        # Reject all cookies
        self.APP.first_page.reject_all_cookies()
        # Search in google
        self.APP.first_page.send_text_in_google_search('Flying Dutchman')
        # Click on first element
        self.APP.first_page.click_on_first_element()
        print('It works!')
