import allure
from fw.web.any_page import AnyPage


class Locator:
    reject_all_cookies = '//div[text()="Отклонить все" or text()="Reject all"]'
    google_search = '//textarea[@title="Поиск"]'
    first_element_in_the_drop_down_list = '(//div[@role="presentation"]//li)[1]'


class FirstPage(AnyPage):

    @allure.step('Reject all cookies')
    def reject_all_cookies(self):
        self.click_element(Locator.reject_all_cookies)

    @allure.step('Send text in google search')
    def send_text_in_google_search(self, text):
        self.send_keys(Locator.google_search, text)

    @allure.step('Сlick on the first item in the drop-down list')
    def click_on_first_element(self):
        self.click_element(Locator.first_element_in_the_drop_down_list)