#!/usr/bin/env python3

from flask import Flask
from flask import request
import jwt
import json
import argparse
import config
import app as app_mod
import logging

def main():
    parser = argparse.ArgumentParser(description="""
        Service to send data to database 
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    confs = config.ConfigManager()

    if args.config is not None:
        with open(args.config, "r") as conffile:
            confs.load_from_file(conffile)
    
    logging.basicConfig(level=getattr(logging, confs["LogLevel"].upper()))

    app = app_mod.create_app(confs.value)
    
    app.run(
        debug=True,
        host=confs["address"],
        port=confs["port"],
    )

if __name__ == '__main__':
    main()
