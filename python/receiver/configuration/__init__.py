from .configurator import Configurator
from os import environ

CONFIG_ENV_NAME = 'CONFIG'
CONFIG_DEFAULT_PATH = 'config.yml'

CONFIG_PATH = environ[CONFIG_ENV_NAME] if CONFIG_ENV_NAME in environ else CONFIG_DEFAULT_PATH

_configuration = Configurator(CONFIG_PATH)

__all__ = [
    'config_flask',
]

config_flask = _configuration['flask']
