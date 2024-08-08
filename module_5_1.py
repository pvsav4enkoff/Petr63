class House():
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        print(f"Название: {self.name}, кол-во этажей: {str(self.number)}")
        return "Название: "+self.name+", кол-во этажей: " +str(self.number_of_floors)

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
# h1.go_to(7)
# h2.go_to(10)
#__str__
print(h1)
print(h2)
#__len__
print(len(h1))
print(len(h2))
