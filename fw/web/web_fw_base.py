from fw.fw_base import FWBase

import allure


class WebFwBase(FWBase):

    def get_page(self):
        if self.manager.browser_manager.page is None:
            self.manager.browser_manager.get_browser()
        return self.manager.browser_manager.page

    @allure.step('Take a screenshot')
    def allure_screenshot(self, full_page=False):
        try:
            screenshot = self.get_page().screenshot(full_page=full_page)
            allure.attach(screenshot, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(str(e))

    @allure.step('Open main page')
    def open_main_page(self):
        self.goto_url(self.manager.settings.GLOBAL[self.manager.settings.branch]['URL'])
        return self

    @allure.step('GoTo URL - {page}')
    def goto_url(self, page):
        current_url = self.get_current_url()
        # Если текущий URL не совпадает с переданным, переходим по новому URL
        if page not in current_url:
            self.get_page().goto(page)

    @allure.step('Click')
    def click_element(self, locator):
        try:
            self.get_page().click(locator)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Send keys')
    def send_keys(self, locator, text):
        try:
            self.get_page().fill(locator, text)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Clear and send keys slow')
    def clear_and_send_keys_slow(self, locator, text, delay=100):
        try:
            input_field = self.get_page().locator(locator)
            # Remove text from field
            input_field.fill("")
            input_field.type(text, delay=delay)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Get input value from field')
    def get_input_value(self, locator):
        try:
            input_value = self.get_page().locator(locator).input_value()
            return input_value

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Get text from field')
    def get_tag_text(self, locator):
        try:
            text = self.get_page().locator(locator).text_content()
            return text

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Get tag attribute from field')
    def get_tag_attribute(self, locator, attribute_name):
        try:
            tag_attribute = self.get_page().locator(locator).get_attribute(attribute_name)
            return tag_attribute

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Get tag attribute from field')
    def get_tag_attributes(self, locator, attribute_name):
        tag_attributes = self.get_page().locator(locator)
        count = tag_attributes.count()

        list_tag_attributes = []
        for i in range(count):
            element = tag_attributes.nth(i).get_attribute(attribute_name)
            list_tag_attributes.append(element)

        return list_tag_attributes


    @allure.step('Clear text from field')
    def clear_keys(self, locator):
        try:
            input_field = self.get_page().locator(locator)
            input_field.fill("")

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    def get_current_url(self):
        return self.get_page().url

    @allure.step('Right click')
    def right_click(self, locator):
        try:
            self.get_page().locator(locator).click(button="right")

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Double click')
    def double_click(self, locator):
        try:
            self.get_page().dblclick(locator)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Refresh page')
    def refresh_the_page(self):
        try:
            self.get_page().reload()

        except TimeoutError as e:
            self.allure_TimeoutError(e)

    @allure.step('Send keys slow')
    def send_keys_slow(self, locator, text, delay=100):
        try:
            input_field = self.get_page().locator(locator)
            input_field.type(text, delay=delay)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Find element')
    def find_element(self, locator):
        try:
            web_element = self.get_page().locator(locator)
            return web_element

        except:
            self.allure_screenshot()
            raise

    @allure.step('Find elements')
    def find_elements(self, locator):
        try:
            web_elements = self.get_page().locator(locator)
            return web_elements

        except:
            self.allure_screenshot()
            raise

    @allure.step('Обработка ошибки, если элемент не найден вовремя')
    def allure_TimeoutError(self, exception_text):
        self.allure_screenshot()
        print(f"TimeoutError occurred: {exception_text}")
        assert True == False  # Останавливаем тест

    @allure.step('Обработка других ошибок')
    def allure_GenericError(self, exception_text):
        self.allure_screenshot()
        print(f"GenericError occurred: {exception_text}")
        assert True == False  # Останавливаем тест