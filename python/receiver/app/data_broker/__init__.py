from .data_broker import DataBroker
from configuration import config_rabbit

data_broker = DataBroker(
    host=config_rabbit['host'],
    port=config_rabbit['port'],
)
