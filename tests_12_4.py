import logging
import unittest
from test_runner import RunnerTest

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))


logging.basicConfig(level=logging.INFO,filemode='w',filename='runner_tests.log',format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",encoding="utf-8")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
