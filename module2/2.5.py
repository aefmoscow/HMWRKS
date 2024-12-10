# комментарии не читайте!!! все для обучения на pythontutor.com
def get_matrix(n, m, value):
    matrix = [] #создать пустой список
    for row in range(n): # цикл for для кол-ва строк матрицы, n повторов.
        matrix.append([]) #добавляйте пустой список в список matrix.
        for col in range(m): # цикл for для кол-ва столбцов матрицы, m повторов.
            matrix[row].append([value]) #пополняйте ранее добавленный пустой список значениями value.
    return matrix #После всех циклов верните значение переменной matrix.

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
