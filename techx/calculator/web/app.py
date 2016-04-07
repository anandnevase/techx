# -*- coding: utf-8 -*-
# Author: Anand Nevase <anand.nevase@xoriant.com>
#
# Description: Main flask application for TechX Calculator.
# This serves the static files, exposes the rest apis etc.


import os

# Web.py always expects the static files and templates to be served from
# the same directory as app.py. We have to explicitly change the working
# directory to current directory incase the app.py is to run from anywhere.
mod_abspath = os.path.abspath(__file__)
mod_dname = os.path.dirname(mod_abspath)
os.chdir(mod_dname)


import logging
from flask import request

from techx.calculator.utils.logger import setup_logging
from techx.calculator.web.init_app import app
from techx.calculator.restcontrollers.operators import get_operators
# REST APIs
@app.route('/calculator/v1/operators', methods=['GET'], strict_slashes=False)
def operators():
    return get_operators()

def run_app():

    setup_logging()
    logging.info('Starting TechX Calculator...')
    # Enable auto-reload of code if TECHX_CALCULATOR_AUTO_RELOAD environment variable is set.
    # Useful in refreshing the demo site if new code is checked in.
    autoreload = os.environ.get('TECHX_CALCULATOR_AUTO_RELOAD')
    if autoreload:
        app.run(host='0.0.0.0', port=8080, debug=True)
    else:
        app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    run_app()
