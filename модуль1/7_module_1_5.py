immutable_var = 1, 4, 'gtyh'
print('значение tuple', immutable_var)
print(type(immutable_var))
mutable_list = [1, 3, 'lockle', 4 + 5]
# print(type(mutable_list))
print('Изначальное значение mutable_list:', mutable_list)
mutable_list[0] = 2
mutable_list[2] = 'only'
mutable_list[3] = 2 + 89
print('Измененное значение  mutable_list:', mutable_list)
