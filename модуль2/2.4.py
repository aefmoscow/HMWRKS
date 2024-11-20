# дан список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# создать пустые списки  primes и not_primes
primes = []
not_primes = []
# При помощи цикла for переберите список numbers.
for i in range(0, len(numbers)):
    print(numbers[i])
#условия что число простое:
def is_prime(numbers[i]):
    if numbers[i] <= 1:
        return False
    for j in range(2, int(numbers[i]**0.5) + 1):
        if n % j == 0:
            not_primes = numbers[i]
            return False
    primes[i] = numbers[i]
    return True
    
    

  #  is_prime=[True]


print('primes', primes)
print('Not primes',not_primes)
