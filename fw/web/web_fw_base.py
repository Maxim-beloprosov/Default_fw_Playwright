import time

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
        self.get_page().goto(page, wait_until='load')
        self.wait_until_page_is_ready(self.get_page())

    @allure.step('Wait until page is fully loaded and ready')
    def wait_until_page_is_ready(self, page):
        # Ждёт полной загрузки всех сетевых запросов
        page.wait_for_load_state('networkidle')

    @allure.step('Click')
    def click_element(self, locator):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            page.click(locator)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Send keys')
    def send_keys(self, locator, text):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            page.fill(locator, text)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Clear and send keys')
    def clear_and_send_keys(self, locator, text):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            input_field = page.locator(locator)
            # Remove text from field
            input_field.fill("a")
            input_field.fill("")
            input_field.type(text)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Clear and send keys slow')
    def clear_and_send_keys_slow(self, locator, text, delay=100):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            input_field = page.locator(locator)
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
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            input_value = page.locator(locator).input_value()
            return input_value

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Get text from field')
    def get_tag_text(self, locator):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            text = page.locator(locator).text_content()
            return text

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Get tag attribute from field')
    def get_tag_attribute(self, locator, attribute_name):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            tag_attribute = page.locator(locator).get_attribute(attribute_name)
            return tag_attribute

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Get tag attribute from field')
    def get_tag_attributes(self, locator, attribute_name):
        page = self.get_page()
        self.wait_until_page_is_ready(page)
        tag_attributes = page.locator(locator)
        count = tag_attributes.count()

        list_tag_attributes = []
        for i in range(count):
            element = tag_attributes.nth(i).get_attribute(attribute_name)
            list_tag_attributes.append(element)

        return list_tag_attributes


    @allure.step('Clear text from field')
    def clear_keys(self, locator):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            input_field = page.locator(locator)
            input_field.fill("")

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    def get_current_url(self):
        page = self.get_page()
        self.wait_until_page_is_ready(page)
        return page.url

    @allure.step('Right click')
    def right_click(self, locator):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            page.locator(locator).click(button="right")

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Double click')
    def double_click(self, locator):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            page.dblclick(locator)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Refresh page')
    def refresh_the_page(self):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            page.reload()

        except TimeoutError as e:
            self.allure_TimeoutError(e)

    @allure.step('Send keys slow')
    def send_keys_slow(self, locator, text, delay=100):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            input_field = page.locator(locator)
            input_field.type(text, delay=delay)

        except TimeoutError as e:
            self.allure_TimeoutError(e)
        except Exception as e:
            self.allure_GenericError(e)

    @allure.step('Find element')
    def find_element(self, locator, wait=None):
        if wait is None:
            wait = self.manager.settings.time_element_wait
        page = self.get_page()
        self.wait_until_page_is_ready(page)
        web_element = page.locator(locator)
        try:
            web_element.wait_for(state="visible", timeout=wait*1000)
            return web_element
        except TimeoutError:
            self.allure_screenshot()
            raise Exception(f"Элемент '{locator}' не появился за {wait} с")

    @allure.step('Find elements')
    def find_elements(self, locator):
        try:
            page = self.get_page()
            self.wait_until_page_is_ready(page)
            web_elements = page.locator(locator)
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

    @allure.step('Проверка дизейбла нужного поля')
    def check_disable_needed_field(self, locator):
        # Получаем данные атрибута disabled
        if (self.get_tag_attribute(locator, 'disabled') == ''
                or self.get_tag_attribute(locator, 'readonly') == ''):
            return True
        else:
            return False

    @allure.step('Проверка валидации в нужном поле')
    def check_validation_in_needed_field(self, locator, text):
        if text == self.get_tag_text(locator):
            return True
        else:
            return False

    @allure.step('Ожидаем, пока данные в нужном поле прогрузятся')
    def wait_while_data_in_needed_field_will_be_loaded(self, locator, empty_value=False, time_for_wait=2):
        """
        ОЖИДАЕТСЯ ПОДАЧА ЭЛЕМЕНТА INPUT
        """
        count = 0
        if empty_value == True:
            while self.get_tag_attribute(locator, 'value') is None:
                time.sleep(0.1)
                count = count + 0.1
                if count >= time_for_wait:
                    raise
        else:
            while self.get_tag_attribute(locator, 'value') is None or self.get_tag_attribute(locator, 'value') == '':
                time.sleep(0.1)
                count = count + 0.1
                if count >= time_for_wait:
                    raise