import unittest
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest

# Создание TestSuite
suite = unittest.TestSuite()

# Добавление тестов в TestSuite

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создание объекта TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
