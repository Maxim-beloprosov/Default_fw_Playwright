from pathlib import Path


class FWBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def get_project_root(self):
        """Returns project root folder."""
        return Path(__file__).parent.parent

