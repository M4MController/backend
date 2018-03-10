#!/usr/bin/env python3

from app import create_api
from configuration import config_flask

if __name__ == '__main__':
    app = create_api()

    app.run(
        debug=bool(config_flask['debug']),
        host=config_flask['host'],
        port=config_flask['port'],
    )
