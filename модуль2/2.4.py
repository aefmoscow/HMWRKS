# дан список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# создать пустые списки  primes и not_primes
primes = []
not_primes = []
# условия что число простое:
def is_prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return primes[1]
    return True
# При помощи цикла for переберите список numbers.
for i in range(0, len(numbers)):
    k = numbers[i]
    print(k)


print('primes', primes[1])
print('Not primes', )
