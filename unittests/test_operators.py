#!/usr/bin/env python
#
# Author: anand.nevase@xoriant.com
#
# Description: Tests for HTTP/REST interface for operators.


import unittest
import json
from mock import patch, MagicMock
from techx.calculator.web.app import app

class TestOperators(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def create_patch(self, *args, **kwargs):
        patcher = patch(*args, **kwargs)
        mock = patcher.start()
        self.addCleanup(patcher.stop)
        return mock

    def test_GET_operators_success(self):
        mock_logger = self.create_patch(
            "techx.calculator.restcontrollers.operators.log")
        expected_resp=['add','subtract']
        resp = self.app.get('/calculator/v1/operators')
        self.assertEqual(resp.data, json.dumps(expected_resp))

    def test_GET_engagements_failure(self):
        mock_logger = self.create_patch(
            "techx.calculator.restcontrollers.operators.log")
        mock_dir = self.create_patch('__builtin__.dir')
        mock_dir.side_effect = Exception()
        resp = self.app.get('/calculator/v1/operators')
        self.assertEqual(resp.status_code, 500)


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOperators)
    return suite

if __name__ == '__main__':
    unittest.main()
