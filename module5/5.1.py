class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, number_of_floors):
        if number_of_floors > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for f in range(1, number_of_floors + 1):
                print(f)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
