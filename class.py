class Dog():
    """Простая модель собаки."""
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age
    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")

myDog=Dog('Terri',11)
print(myDog.name.title())
myDog.sit()
myDog.roll_over()

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print('\n'+self.restaurant_name+' open in '+ self.cuisine_type)

rest=Restaurant('Gulli',"France")
rest.describe_restaurant()
rest=Restaurant('Pogani',"Ital")
rest.describe_restaurant()
rest=Restaurant('MacDonald',"USA")
rest.describe_restaurant()

class User():
    def __init__(self,first_name,last_name,age,prazd):
        self.first_name = first_name
        self.last_name=last_name
        self.age=age
        self.prazd=prazd

    def svodka(self):
        print(self.first_name.title() +' '+ self.last_name.title()+' age '+str(self.age))
    def pozdr(self):
        print(self.first_name.title() + ' ' + self.last_name.title() + '  ' + str(self.prazd))


us=User('Petr','Vladimirovich',61,"S Novym Godom!")
us.svodka()
us.pozdr()