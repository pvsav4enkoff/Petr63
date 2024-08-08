class Figure:
    sides_count = 0
    def __init__(self, color, sides):
        print('Figure')
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, side):
        print('Circle')
        super().__init__(color, [side])

        self.__radius = side / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        print("Triangle",sides)
        # print(self.get_sides())
        super().__init__(color, [sides]*3)
        print(self.get_sides())
        # a, b, c = self.get_sides()
        # self.__height = 2 * (a * b * c) / (a ** 2 + b ** 2 + c ** 2)

    def get_square(self):
        print(self.get_sides())
        a, b, c = self.get_sides()
        self.__height = 2 * (a * b * c) / (a ** 2 + b ** 2 + c ** 2)
        return 0.5 * a * self.__height

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        print('Cube')
        super().__init__(color,[sides] * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 100, 10), 7)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
triangle1.set_color(200, 100, 15) # Не изменится
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
triangle1.set_sides(22,22,30) # Изменится
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print(triangle1.get_square())
