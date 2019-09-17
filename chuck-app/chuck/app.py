#!/usr/bin/env python

from flask import Flask, Response, request
from datetime import datetime
import requests
import logging
import os
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger

app = Flask("chuck")

STATUS_500='Internal error'
STATUS_404='Not found'
STATUS_405='Method not allowed'


@app.route("/")
def chuckNorris():
    url = 'https://api.chucknorris.io/jokes/random'
    r = requests.get(url)
    if r.status_code == 200:
        local = datetime.now()
        xablam = r.json()['value']
        user_agent = request.headers.get('User-Agent')
        host = request.remote_addr
        path = request.path
        method = request.method
        st = "200 777"
        protocol = request.environ.get('SERVER_PROTOCOL')
        app.logger.info('{0} - - [{1}] "{2} {3} {4}" {5} "-" "{6}"'.format(host, 
                                                                           local.strftime("%b/%d/%Y:%H:%M:%S"), 
                                                                           method, 
                                                                           path, 
                                                                           protocol, 
                                                                           st, 
                                                                           user_agent))
        return xablam


@app.errorhandler(404)
def not_found(exception):
    user_agent = request.headers.get('User-Agent')
    local = datetime.now()
    host = request.remote_addr
    path = request.path
    method = request.method
    st = "404 666"
    protocol = request.environ.get('SERVER_PROTOCOL')
    app.logger.error('{0} - - [{1}] "{2} {3} {4}" {5} "-" "{6}"'.format(host, 
                                                                        local.strftime("%b/%d/%Y:%H:%M:%S"), 
                                                                        method, 
                                                                        path, 
                                                                        protocol, 
                                                                        st, 
                                                                        user_agent))
    return Response(STATUS_404, status=404)

@app.errorhandler(405)
def not_allowed(exception):
    user_agent = request.headers.get('User-Agent')
    local = datetime.now()
    host = request.remote_addr
    path = request.path
    method = request.method
    st = "405 666"
    protocol = request.environ.get('SERVER_PROTOCOL')
    app.logger.error('{0} - - [{1}] "{2} {3} {4}" {5} "-" "{6}"'.format(host, 
                                                                        local.strftime("%b/%d/%Y:%H:%M:%S"), 
                                                                        method, 
                                                                        path, 
                                                                        protocol, 
                                                                        st, 
                                                                        user_agent))
    return Response(STATUS_405, status=405)

@app.errorhandler(500)
def not_found(exception):
    user_agent = request.headers.get('User-Agent')
    local = datetime.now()
    host = request.remote_addr
    path = request.path
    method = request.method
    st = "500 666"
    protocol = request.environ.get('SERVER_PROTOCOL')
    app.logger.error('{0} - - [{1}] "{2} {3} {4}" {5} "-" "{6}"'.format(host, 
                                                                        local.strftime("%b/%d/%Y:%H:%M:%S"), 
                                                                        method, 
                                                                        path, 
                                                                        protocol, 
                                                                        st, 
                                                                        user_agent))
    return Response(STATUS_500, status=500)


if __name__ == "__main__":
    
    DEBUG=False

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    log.disabled = True
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'

    logging.basicConfig(level=logging.FATAL)

    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    app.run(host='0.0.0.0', port=9667, debug=False)
    # app.run(debug=False)
