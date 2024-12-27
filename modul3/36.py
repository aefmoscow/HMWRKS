# Исходный объект типа список
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(dat):
    global summa
    for el in dat:
        if isinstance(el, dict):
            calculate_structure_sum(el.items())
        elif isinstance(el, (list, tuple, set)):
            calculate_structure_sum(el)
        elif isinstance(el, str):
            summa += len(el)
        elif isinstance(el, (int, float)):
            summa += el
    return summa


summa = 0
result = calculate_structure_sum(data_structure)
print(result)

# Проверялка понятная (Вопрос: почему №2неверно выдает сумму построчно???Пусть бы по нарастающей, но криво считает)
# for i in range(len(data_structure)):
#     print('Elem  ', i, type(data_structure[i]), data_structure[i])
# 2 print('Elem  ', i, type(data_structure[i]), data_structure[i], 'Сумма ', calculate_structure_sum(data_structure[i]))
