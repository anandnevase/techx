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



# REST APIs
@app.route('/xporter/v1/eula', methods=['POST'], strict_slashes=False)

def run_app():

    setup_logging()
    logging.info('Starting AMF Xporter...')
    # Enable auto-reload of code if XPLORER_AUTO_RELOAD environment variable is set.
    # Useful in refreshing the demo site if new code is checked in.
    autoreload = os.environ.get('XPORTER_AUTO_RELOAD')
    if autoreload:
        app.run(host='0.0.0.0', port=8080, debug=True)
    else:
        app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    run_app()
