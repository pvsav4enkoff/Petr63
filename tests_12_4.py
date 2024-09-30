import logging
import unittest
from tests_12_2 import TournamentTest

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))


logging.basicConfig(level=logging.INFO,filemode='w',filename='runner_tests.log',format="%(asctime)s | %(levelname)s | %(message)s",encoding="utf-8")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)