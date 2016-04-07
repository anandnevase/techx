from flask import jsonify
from techx.calculator.web.init_app import app


class CustomWebException(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        return_value = dict(self.payload or ())
        return_value['message'] = self.message
        return_value['status'] = self.status_code
        return return_value


@app.errorhandler(CustomWebException)
def handle_custom_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
