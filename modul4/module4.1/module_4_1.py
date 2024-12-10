from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
print('Результат 1: ', result1)
print('Результат 2: ', result2)

result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print('Результат 3: ', result3)
print('Результат 4: ', result4)
