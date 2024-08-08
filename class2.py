from class1 import TriClass
from module_5_1 import House

# x=TriClass("na ugle","Shashl")
# y=TriClass("na masle",'mangal')
# x.setdata("1111-2222")
# y.setdata("3333-4444")
# x.display()
# x.setprn()
# y.display()
# y.setprn()
#
# # x.dataS
# print(x.restaurant_name,x.cuisine_type,y.restaurant_name,y.cuisine_type,x.dataS)
# x.dataS = "14-06-24"
# # x=TriClass("na ugle","Shashl")
# print(x.restaurant_name,x.cuisine_type,y.restaurant_name,y.cuisine_type,x.dataS)
class House1(House):
    pass
    # def go_to(self,num):
    #     num_save=7
    #     if num != 0:
    #         print('Это другой класс', num)
    #     else:
    #         print('равно ',num_save)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(7)
h2.go_to(10)
h3=House1('ЖК Горский', 18)
h3.num_save=4
h3.go_to(25)