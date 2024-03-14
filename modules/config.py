import os
import json
from .logger import Logger

logger = Logger()

class Config:
    def __init__(self):
        self.config_file = "config.json"
        self.config = {}

    def load(self):
        # Check if the config file exists
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as file:
                self.config = json.load(file)
        else:
            self.config = {}
            self.save()

    def save(self):
        with open(self.config_file, "w") as file:
            json.dump(self.config, file, indent=4)
            logger.log(f"Config file saved at {self.config_file}")
