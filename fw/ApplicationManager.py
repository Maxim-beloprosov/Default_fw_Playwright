from data.settings import Settings
from fw.BrowserManager import BrowserManager
from fw.api.petstore.user.api_actions_in_user import ApiActionsInUser
from fw.web.any_page import AnyPage
from fw.web.google.first_page import FirstPage
from fw.web.web_fw_base import WebFwBase
from fw.fw_base import FWBase
from data.group_data import GroupData


class ApplicationManager:

    def __init__(self):
        # Common
        self.browser_manager = BrowserManager()
        self.fw_base = FWBase(self)
        self.settings = Settings()
        self.group_data = GroupData()

        # WEB
        self.web_fw_base = WebFwBase(self)
        self.any_page = AnyPage(self)
        self.first_page = FirstPage(self)

        # API
        self.api_actions_in_user = ApiActionsInUser(self)

