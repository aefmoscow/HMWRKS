def summa(n):
    if n == 0:
        return 0
    else:
        return  n  +  summa(n   -   1)

print(summa(5))

def pr_summa(n):
    x = 0
    for n in range(1, n + 1):
        x += n
    return x

print(pr_summa(5))