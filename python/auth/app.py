#!/usr/bin/env python3

from flask import Flask
import jwt
jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

app = Flask(__name__)

@app.route('/sign_in')
def hello_world():
    token = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    return token


def main():
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000,
    )

if __name__ == '__main__':
    main()
