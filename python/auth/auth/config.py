import json
import time

class ConfigManager(object):
    default = {
        "address": "0.0.0.0",
        "port": 5000,
    }

    def __init__(self):
        self.value = dict(ConfigManager.default)

    def load_from_file(self, file):
        loaded = json.load(file)
        self.value = ConfigManager.__merge_loaded(dict(self.default), loaded)

    def load_from_string(self,string):
        loaded = json.loads(string)
        self.value = ConfigManager.__merge_loaded(dict(ConfigManager.default), loaded)
    
    def __getitem__(self, key):
        return self.value[key]

    @staticmethod
    def __merge_loaded(default, loads):
        for name, val in loads.items():
            if type(val) is dict:
                default[name] = ConfigManager.__merge_loaded(default[name], val)
            else:
                default[name] = val
        return default
