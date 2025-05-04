from fw.ApplicationManager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_module(self):
        pass

    def setup_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def teardown_class(self):
        pass

    def teardown_module(self):
        pass