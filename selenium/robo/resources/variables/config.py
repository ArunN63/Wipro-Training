import yaml
from resources.variables.environments import ENVIRONMENT


class Config:

    def __init__(self):
        config_file = f"config/{ENVIRONMENT}.yaml"
        with open(config_file, "r") as file:
            self.data = yaml.safe_load(file)

    @property
    def base_url(self):
        return self.data["application"]["url"]

    @property
    def browser(self):
        return self.data["browser"]["name"]

    @property
    def headless(self):
        return self.data["browser"]["headless"]

    @property
    def implicit_wait(self):
        return self.data["timeouts"]["implicit_wait"]

    @property
    def explicit_wait(self):
        return self.data["timeouts"]["explicit_wait"]

    @property
    def report_path(self):
        return self.data["reporting"]["report_path"]

    @property
    def screenshot_path(self):
        return self.data["reporting"]["screenshot_path"]


config = Config()