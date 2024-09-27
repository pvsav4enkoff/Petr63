import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
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
                # print(participant)
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    # print(place,participant,participant.speed)
                    place += 1
                    self.participants.remove(participant)
        # print(finishers.keys(),finishers.values())
        return finishers
class TournamentTest(unittest.TestCase):
    # def __init__(self,finishers):
    #     self.finishers = finishers
    #     self.all_results = {}

    def setUpClass(self):
        # for key, value in self.finishers.items():
        self.all_results = {}

    def setUP(self):
        self.nick = Runner("Ник", 3)
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
    def tearDownClass(self):
        for key, value in self.all_results.items():
            print(f"Результат теста {key}: {value}")

        pass
    def usein_nic(self):
        t = Tournament(90, self.usain, self.nick)
        result = t.start()
        self.all_results[len(self.all_results)] = result
        self.assertTrue(list(result.keys())[-1] == "Ник")
    def andrey_nic(self):
        t = Tournament(90, self.andrey, self.nick)
        result = t.start()
        self.all_results[len(self.all_results)] = result
        self.assertTrue(list(result.keys())[-1] == "Ник")

    def usein_andrey_nic(self):
        t = Tournament(90, self.usain, self.andrey,self.nick)
        result = t.start()
        self.all_results[len(self.all_results)] = result
        self.assertTrue(list(result.keys())[-1] == "Ник")
test=TournamentTest()
# test.usein_nic()
# test.andrey_nic()
# test.usein_andrey_nic()
# r1=Runner("Ник",3)
# r2=Runner("Усэйн",10)
# r3=Runner("Андрей",9)
#
# rez=Tournament(90,r1,r2,r3)
# s=rez.start()
# z=TournamentTest(s)
# t=z.setUpClass()
# z.setUP()
# t.Nic

# for i in s:
#     print(i.__str__())
# for key, value in s.items():
#     print(f"{key}: {value}")
# print(rez.start())

# print(rez.start,rez.participants,rez.full_distance)