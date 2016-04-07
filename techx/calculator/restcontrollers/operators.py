#
# Author : anand.nevase@xoriant.com
#
# Description: HTTP/REST interface for getting list of existing Calculator Operators.
#


import os
import json
import logging
from techx.calculator import config
from techx.calculator.web.exception_handler import CustomWebException
from techx.calculator.calculator import TechxCalculator

log = logging.getLogger(__name__)


def get_operators():
    operator = []
    try:
         operator= [name for name in dir(TechxCalculator) if not name.startswith('_')]
         
    except Exception as exception:
        log.exception(
            "Failed to fetch operators details"
        )
        raise CustomWebException(
            "Failed to fetch operators details : " + str(exception), 500)

    return json.dumps(operator)
