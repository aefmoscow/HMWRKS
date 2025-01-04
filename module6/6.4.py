class Figure:
    sides_count = 0
    __sides
    filled
    def get_color
    def  __is_valid_color
    def set_color
    def __is_valid_sides
    def get_sides
    def __len__
    def  set_sides(self, *new_sides)

class Circle(Figure):
    sides_count = 1
    __radius =
    def get_square
class Triangle(Figure) :
    sides_count = 3
    def get_square

class Cube(Figure):
    sides_count = 12
    new!!!__sides
    def get_volume



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:

circle1.set_color(55, 66, 77)  # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится

print(cube1.get_color())

# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится

print(cube1.get_sides())

circle1.set_sides(15)  # Изменится

print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:

print(len(circle1))

# Проверка объёма (куба):

print(cube1.get_volume())

