# комментарии не читайте!!! все для обучения на pythontutor.com ;)

numbers = [-10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# При помощи цикла for переберите список numbers.
for dig in numbers:
    is_prime = True
    for divider in range(2, dig):
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
        if dig % divider == 0:
            is_prime = False
            not_primes.append(dig)
            break
    if is_prime == True and dig != 1 and dig != 0 and dig > 0:
        primes.append(dig)

print(f'Primes: {primes} ')
print(f'Not Primes: {not_primes}')
