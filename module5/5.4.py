class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
    houses_history = []

    # Дополняем метод __new__ так, чтобы:
    # Название объекта добавлялось в список cls.houses_history.
    # Название строения можно взять из args по индексу.

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    # Переопределяем метод __del__(self) в котором будет выводиться строка:

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3

print(House.houses_history)
