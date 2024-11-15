grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Преобразование множества в список
list_students = list(students)
# Сортировка списка
sorted_list_students = sorted(list_students)
# вычисляем среднее
middle_grades = (
    (sum(grades[0])) / len(grades[0]), (sum(grades[1])) / len(grades[1]), (sum(grades[2])) / len(grades[2]),
    (sum(grades[3])) / len(grades[3]), (sum(grades[4])) / len(grades[4]))
# Составляем словарь
my_dict = {sorted_list_students[0]: middle_grades[0], sorted_list_students[1]: middle_grades[1],
           sorted_list_students[2]: middle_grades[2], sorted_list_students[3]: middle_grades[3],
           sorted_list_students[4]: middle_grades[4]}
print(my_dict)*2
