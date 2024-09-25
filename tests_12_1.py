import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10
    def walk(self):
        self.distance += 5
    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        t = Runner("walk")

        for i in range(0,10):
            t.walk()
        self.assertEqual(t.distance,50,"test_walk")
    def test_run(self):
        t = Runner("run")
        for i in range(0, 10):
            t.run()
        self.assertEqual(t.distance,100,"test_run")
    def test_challenge(self):
        t1 = Runner("run")
        t2 = Runner("walk")
        for i in range(1, 10):
            t1.walk()
            t2.run()
        self.assertNotEqual(t1.distance,t2.distance,"test_challenge")

RunnerTest()
