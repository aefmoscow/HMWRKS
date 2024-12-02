data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
for i in range(len(data_structure)):
  print('Elem  ', i, type(data_structure[i]), data_structure[i])
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

def calculate_structure_sum(data_structure):
  global  summ
  for i in range(len(data_structure)):
    if isinstance(data_structure[i], str):

summ = 0
# result = calculate_structure_sum(data_structure)

# print(result)