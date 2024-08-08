from colorama import init, Fore, Back, Style
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self,owner,model,color,engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f"Модель: {self.__model}"
        # print(self.__model)
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
        # print(self.__engine_power)
    def get_color(self):
        return f"Цвет: {Fore.GREEN} {self.__color}"
        # print(self.__color)
    def print_info(self):
        print(Fore.BLUE + self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(Fore.BLUE + f"Владелец: {Fore.GREEN} {self.owner}")
    def set_color(self, new_color):
        for color in self.__COLOR_VARIANTS:
            if new_color.lower() in color.lower():
                self.__color = new_color
                break
        else:
            print(Fore.RED + f"Нельзя сменить цвет на {new_color}")
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()




