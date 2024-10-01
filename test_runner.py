import unittest
import logging
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen=False
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        try:
            t = Runner(2)
            for i in range(0,10):
                t.walk()
            self.assertEqual(t.distance,50,t.name)
            logging.info(f" test_walk выполнен успешно")
        except TypeError as exc:
            logging.warning(f" Неверный тип данных для Runner",exc_info=exc)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        try:
            t = Runner("Сергей",-5)
            for i in range(0, 10):
                t.run()
            self.assertEqual(t.distance,100,t.name)
            logging.info(f" test_run выполнен успешно")
        except ValueError as exc:
            logging.warning(f" Неверная скорость для Runner",exc_info=exc)
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_challenge(self):
        try:
            t1 = Runner("Вася")
            t2 = Runner("Сергей")
            for i in range(1, 10):
                t1.walk()
                t2.run()
            self.assertNotEqual(t1.distance,t2.distance,t1.name)
            logging.info(f" test_challenge выполнен успешно")
        except ValueError as exc:
            logging.warning(f" Неверная скорость для Runner", exc_info=exc)

RunnerTest()
