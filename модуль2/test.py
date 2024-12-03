# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return  n  +  summa(n   -   1)
#
# print(summa(5))
#
# def pr_summa(n):
#     x = 0
#     for n in range(1, n + 1):
#         x += n
#     return x
#
# print(pr_summa(5))
data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]
summa=0
def calculate_structure_sum(dat):
    global summa
    for el in dat:
        if isinstance(el, dict):
            calculate_structure_sum(el.items())
        elif isinstance(el, (list, tuple, set)):
            calculate_structure_sum(el)
        elif isinstance(el, str):
            print('str',summa)
            summa += len(el)

        elif isinstance(el, (int, float)):
            print('int, float',summa)
            summa += el


    return summa

#
# def calculate_structure_sum(dat):
#     global summa
#     for el in dat:
#         if isinstance(el, dict):
#             calculate_structure_sum(el.items())
#         elif isinstance(el, (list, tuple, set)):
#             calculate_structure_sum(el)
#         elif isinstance(el, str):
#             summa += len(el)
#         elif isinstance(el, (int, float)):
#             summa += el
#     return summa
#
#
# summa = 0
result = calculate_structure_sum(data_structure)
print(result)