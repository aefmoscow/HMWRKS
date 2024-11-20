# комментарии не читайте!!! все для обучения на pythontutor.com ;)

numbers = [-10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# При помощи цикла for переберите список numbers.

for elem in numbers:
    is_prime = True
    for divider in range(2,
                         elem):  # Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
        if elem % divider == 0:
            is_prime = False
            not_primes.append(elem)
            break  # Попробуйте ускорить процесс выяснения простоты числа при помощи оператора break, когда найдёте делитель.
    if is_prime == True and elem != 1 and elem != 0 and elem > 0:
        primes.append(elem)

print(f'Primes: {primes} ')
print(f'Not Primes: {not_primes}')
