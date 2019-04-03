#!/usr/bin/env python3

from flask import Flask
from flask import request
import jwt
import json
import argparse
import config
import app as app_mod
import logging

app = None

def main(conf, run_me=False):
    confs = config.ConfigManager()
    if conf is not None:
        with open(conf, "r") as conffile:
            confs.load_from_file(conffile)
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    app = app_mod.create_app(confs.value)
    if run_me:
        app.run(
            debug=True,
            host=confs["address"],
            port=confs["port"],
        )
    return app  

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
        Service to send data to database 
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    conf = args.config
    main(conf, run_me=True)
