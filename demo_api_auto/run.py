import HTMLTestRunnerNew
from demo_api_auto.tools.test_http_request import TestHttpRequest
import unittest
from demo_api_auto.tools.project_path import *

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
with open(test_report_path, "wb") as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title=None, descrition=None, tester=None)
    runner.run(suite)
