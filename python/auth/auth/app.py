#!/usr/bin/env python3

from flask import Flask
from flask import request
import jwt
import json
from auth.view.sing_in import sign_in_schema
import argparse
import config 

app = Flask(__name__)

SECURE_KEY = "REMOVE_ME_PLEASE"

@app.route('/sign_in', methods = ['POST',])
def hello_world():
    data = request.get_json(force=True)
    data_cleaned = sign_in_schema.load(data)
    data = data_cleaned.data
    if (data['e_mail'] == 'ml@gmail.com') and (data['password'] == '123456'):
        token = jwt.encode({'user_id': 1}, SECURE_KEY, algorithm='HS256')
        return token
    return '', 401


def main():
    parser = argparse.ArgumentParser(description="""
        Service to store objects
    """)
    parser.add_argument('--config', help='configuration file', default=None)
    args = parser.parse_args()
    confs = config.ConfigManager()
    if args.config is not None:
        with open(args.config, "r") as conffile:
            confs.load_from_file(conffile)
    app.run(
        debug=True,
        host=confs["address"],
        port=confs["port"],
    )

if __name__ == '__main__':
    main()
