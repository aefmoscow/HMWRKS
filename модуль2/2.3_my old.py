# комментарии не читайте!!! все для обучения ;)
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# назначаем переменную номера элемента
el_ind = 0
itemlist=[]
while el_ind < len(my_list):
    item = my_list[el_ind]
    el_ind = el_ind + 1
    if item == 0:
        continue
    elif item < 0:
        break
    else:
        itemlist.append(item)
print(*itemlist)
        # print(item)