import traceback
import logging
from flask import Flask, jsonify
import sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("test", file=sys.stderr)
    return {"demo": "test"}


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
