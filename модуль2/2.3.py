# проверочная строка на выход диапазона
# my_list = [42, 69, 322, 13, 0, 99, 5, 9, 8, 7, 6, 5]
# начало программы
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
inn = 0
l = len(my_list) - 1
# print('Eto L', l)
while my_list[inn] > 0:
    print(my_list[inn])
    inn = inn + 1
    if my_list[inn] == 0:
        inn = inn + 1
    elif inn == l:
        break
    continue
