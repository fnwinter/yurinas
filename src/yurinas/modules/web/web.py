# Copyright 2019 fnwinter@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from flask import Flask, jsonify

from base.path.path import STATIC_RESOURCE_PATH
from utils.log import get_logger

app = Flask(__name__, static_url_path='', static_folder=STATIC_RESOURCE_PATH)

log = get_logger('WEB')

@app.route('/')
def root():
    global app
    return app.send_static_file("index.html")

@app.route('/login')
def login():
    global app
    return app.send_static_file("index.html")

@app.route('/login_request', methods=['POST'])
def login_test():
    return jsonify({'test':'1234'})

def process_main(_):
    global app
    global log
    try:
        log.info("WEB Process start")
        app.run(host='0.0.0.0', port='8080', use_reloader=False, debug=True)
        log.info("WEB Process end")
    except Exception as e:
        log.info("WEB Module error %s", e)