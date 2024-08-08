# Добавлен подкласс, адаптирующий поведение суперкласса
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return "[Person: %s, %s]" % (self.name, self.pay)
class Manager(Person):
    def __init__(self, name, pay):  # Переопределенный конструктор
        Person.__init__(self, name, "mgr", pay)  # Вызов оригинального
    # конструктора со значением
    # ‘mgr’ в аргументе job
    def giveRaise(self, percent, bonus=.10): # Переопределение метода
        Person.giveRaise(self, percent + bonus) # Вызов версии из
# класса Person
if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
tom = Manager("Tom Jones", 50000) # Экземпляр Manager: __init__
tom.giveRaise(.10) # Вызов адаптированной версии
print(tom.lastName()) # Вызов унаследованного метода
print(tom) # Вызов унаследованного __str__
print("--All three--")
for object in (bob, sue, tom): # Обработка объектов обобщенным способом
    object.giveRaise(.10) # Вызовет метод giveRaise этого объекта
    print(object) # Вызовет общий метод __str__