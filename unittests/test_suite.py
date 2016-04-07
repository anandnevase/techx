# Author: anand.nevase@xoriant.com
#
# Description: Test suite for running all tests. Run : python test_suite.py

import unittest
import sys
import test_operators

if __name__ == "__main__":
    operators_suit = test_operators.suite()

    all_tests = unittest.TestSuite([operators_suit])

    return_value = unittest.TextTestRunner(
        verbosity=2).run(all_tests).wasSuccessful()
    if return_value:
        sys.exit(0)
    else:
        sys.exit(1)
