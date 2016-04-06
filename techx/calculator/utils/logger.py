#!/usr/bin/env python
#
#
# Author: Anand Nevase <anand.nevase@xoriant.com>
#
# Description: Setup logging for TechX Calculator app.


import os
import logging
import logging.handlers

from techx.calculator import config


def setup_logging():
    """Setup application logging.
    """
    # Create directory if not present
    if not os.path.exists(config.logs_dir):
        os.makedirs(config.logs_dir)

    path = os.path.join(config.logs_dir, config.log_conf.get(
        'filename', 'calculator.log'))
    format = config.log_conf.get(
        'formatter', '%(name)s: %(asctime)s %(levelname)s  %(message)s')
    level = getattr(logging, config.log_conf.get('level', 'DEBUG'))
    maxBytes = int(config.log_conf.get('maxBytes', 1024 * 1024))
    backupCount = int(config.log_conf.get('backupCount', 5))

    loghandler = logging.handlers.RotatingFileHandler(
        path, maxBytes=maxBytes, backupCount=backupCount)
    formatter = logging.Formatter(format)
    loghandler.setFormatter(formatter)

    rootlogger = logging.getLogger()
    rootlogger.setLevel(level)
    rootlogger.addHandler(loghandler)
