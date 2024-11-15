my_dict = {'Denis': 1999, 'Petr': 2000}
print(my_dict)
print('Existing value:', my_dict['Denis'])
print('Non Existing value:', my_dict.get('Perrrr'))
my_dict.update({'Elza': 12354, 'Zuzi': 568989})
print(my_dict)
print('Deleted value:', my_dict['Elza'])
del my_dict['Elza']
print('Modified dictionary:', my_dict)
# end of part 1
my_set = {1.14, 'False', 'Then', 56, 7, 'False', 1.14}
print('Set: ', my_set)
my_set.update({55555, 66666})
my_set.discard(56)
print('Modified Set: ', my_set)
