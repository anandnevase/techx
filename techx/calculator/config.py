# -*- coding: utf-8 -*-
#
# Author: Anand Nevase
#
# Description: TECHX Calculator configureable options


import os


# User configurable settings via environment variables
# conf_dir = os.environ.get('XPORTER_CONF_DIR') or os.path.join(
#     os.path.expanduser('~/xporter'), 'conf')
# logs_dir = os.environ.get('XPORTER_LOGS_DIR') or os.path.join(
#     os.path.expanduser('~/xporter'), 'logs')
# if os.environ.get('XPORTER_ENV') == 'DEV':
#     log_level = os.environ.get('XPORTER_LOG_LEVEL', 'DEBUG').upper()
# else:
#     log_level = os.environ.get('XPORTER_LOG_LEVEL', 'INFO').upper()
# filestore = os.environ.get('XPORTER_JSON_DIR') or os.path.join(
#     os.path.expanduser('~/xporter'), 'engagements')
# eulastore = os.environ.get('XPORTER_EULA_FILE') or os.path.join(
#     os.path.expanduser('~/xporter'), 'eula.json')

log_conf = {
    "filename": "calculator.log",
    "formatter": "%(name)s: %(asctime)s %(levelname)s  %(message)s",
    "level": log_level,
    "maxBytes": 1048576,
    "backupCount": 5
}