first = input('Input first ')
second = input('Input second ')
Third = input('Input Third ')
# print(first, second, Third)
if first == second == Third:
    print('Vse ravni,', 3)
elif first == second or second == Third or first == Third:
    print('Poparno  ravni,', 2)
# можно и так
# elif first != second and  second != Third  and first !=  Third :
else:
    print('Ne  ravni,', 0)
