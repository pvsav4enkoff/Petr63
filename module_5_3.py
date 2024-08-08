class House():
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __add__(self, value):
        self.number_of_floors += value
        return self
    # def __iadd__(self, value):
    #     self.number_of_floors=self.number_of_floors + value
    #     return self
    def __radd__(self, value):
        self.number_of_floors=self.number_of_floors + value
        return self
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return "Название: "+self.name+", кол-во этажей: " +str(self.number_of_floors)
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return
    def go_to(self,new_floor):
        if new_floor > 0 and new_floor <= self.number_of_floors:
            i = 1
            while i <= new_floor:
                print(i)
                i += 1
        else:
            print(f"{self.name} Такого этажа не существует")

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#__str__
print(h1)
print(h2)

print(h1 == h2) # __eg__

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
