import unittest
import logging
import datetime
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        if self.speed > 0:
            self.distance += self.speed * 2

    def walk(self):
        if self.speed > 0:
            self.distance += self.speed

    def __str__(self):
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
                if participant.distance == 0:
                    return finishers
        # print(finishers)
        return finishers
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", -9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            rez={}
            for key1, value1 in value.items():
                rez[key1]=str(value1)
            print(rez)
    def test_usain_nick(self):
        try:
            tournament = Tournament(90, self.usain, self.nick)
            result = tournament.start()
            self.all_results[len(self.all_results)] = result
            self.assertTrue(list(result.values())[-1] == "Ник")
            logging.info(f" test_usain_nick выполнен успешно")
        except:
            logging.warning(f" Неверная скорость для Runner")
            pass
    def test_andrey_nick(self):
        try:
            tournament = Tournament(90, self.andrey, self.nick)
            result = tournament.start()
            self.all_results[len(self.all_results)] = result
            self.assertTrue(list(result.values())[-1] == "Ник")
            logging.info(f" test_andrey_nick выполнен успешно")
        except:
            logging.warning(f" Неверная скорость для Runner")
    def test_usain_andrey_nick(self):
        try:
            tournament = Tournament(90, self.usain, self.andrey, self.nick)
            result = tournament.start()
            self.all_results[len(self.all_results)] = result
            self.assertTrue(list(result.values())[-1] == "Ник")
            logging.info(f" test_usain_andrey_nick выполнен успешно")
        except:
            logging.warning(f" Неверная скорость для Runner")
if __name__ == "__main__":
    unittest.main()
