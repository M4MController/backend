import yaml


class Configurator:
    def __init__(self, config_file):
        with open(config_file, 'r') as yml:
            self.config_file = yaml.load(yml)

    def __getitem__(self, item):
        return self.config_file[item]
