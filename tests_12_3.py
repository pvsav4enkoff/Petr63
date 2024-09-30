import unittest
def skip_if_frozen(func):

    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            print('Тесты в этом кейсе заморожены')
            return
        return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        pass
        # setUpClass

    @skip_if_frozen
    def test_runner(self):
        pass
        # test_runner

class TournamentTest2(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        pass
        # setUpClass

    @skip_if_frozen
    def test_tournament(self):
        # self.assertEqual(t.distance, 100, "test_run")
        # self.assertTrue(True)
        pass
        # test_tournament
