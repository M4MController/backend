from flask import Flask
from flask import request
import jwt
import json
import argparse
import config
import receiver
import logging

def build_app(confs):
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))
    app = receiver.create_app(confs.value)
    return app

def build_config(conf_path=None):
    confs = config.ConfigManager()
    if conf_path is not None:
        with open(conf_path, "r") as conffile:
            confs.load_from_file(conffile)
    return confs

def gunicorn_entry(conf_path=None):
    return build_app(build_config(conf_path))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
        Service to send data to database 
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    conf = args.config
    confs = build_config(conf)
    app = build_app(confs)
    app.run(
        debug=True,
        host=confs["address"],
        port=confs["port"],
    )