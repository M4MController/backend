#!/usr/bin/env python3

from flask import Flask
from flask import request
import jwt
import json
from auth.view.sing_in import sign_in_schema


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
    app.run(
        debug=True,
        host="0.0.0.0",
        port=4999,
    )

if __name__ == '__main__':
    main()
