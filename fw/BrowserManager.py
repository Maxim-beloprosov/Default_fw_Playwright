from playwright.sync_api import sync_playwright
from data.settings import Settings


class BrowserManager:

    def __init__(self):
        self.page = None
        self.playwright = None
        self.browser = None

    def get_browser(self):
        if self.page is None:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=Settings.Browser['headless'],
                                                           args=["--start-maximized"])
            self.page = self.browser.new_page(no_viewport=True)
        return self.page

    def stop_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()