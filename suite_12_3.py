import unittest
from tests_12_3 import TournamentTest2
from tests_12_2 import TournamentTest
# from test_12_3 import TournamentTest

# Создание TestSuite
suite = unittest.TestSuite()

# Добавление тестов в TestSuite
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest2))

# Создание объекта TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
