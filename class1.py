class FirstClass: # Определяет объект класса
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        # self.dataS = "11-07-24"
    def setdata(self, value): # Определяет метод класса
        self.data = value
        self.dataS = "11-07-24"
        # self – это экземпляр
    def display(self):
        print(self.data) # self.data: данные экземпляров
class SecondClass(FirstClass):              # Наследует setdata
    def display(self):                      # Изменяет display
        print("Current value = “%s”" % self.data)
class TriClass(SecondClass):              # Наследует setdata
    def display(self):                      # Изменяет display
        print("Current = “%s”" % self.data)
    def setprn(self):
        print("New def")

x=FirstClass('Na ogne',"Picca")
y=FirstClass("na paru","stolovay")

# x.setdata(12345)
# y.setdata(6789)
# x.display()
# y.display()
#
# print(x.restaurant_name,x.cuisine_type)
#
# x=SecondClass("Na vode","stolovay")
# x.setdata("1111-1111")
# x.display()
# print(x.restaurant_name,x.cuisine_type)
#
# x=TriClass("na ugle","Shashl")
# x.setdata("1111-2222")
# x.display()
# x.setprn()
#
# # x.dataS
# print(x.restaurant_name,x.cuisine_type,x.dataS)
# x.dataS = "14-06-24"
# # x=TriClass("na ugle","Shashl")
# print(x.restaurant_name,x.cuisine_type,x.dataS)

