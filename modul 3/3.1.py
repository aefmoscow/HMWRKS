calls = 0  # Создать переменную calls = 0 вне функций.

# подсчитывающая вызовы остальных функций. Создать функцию count_calls и изменять в ней значение переменной calls.
def count_calls():
    global calls
    calls += 1

# приведем к нижнему индексу
def lower_string(elem):
    a = elem.lower()
    return a

# принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Создать функцию string_info с параметром string
def string_info(string):
    count_calls()
    return f'({len(string)}, {string.upper()}, {string.lower()})'

print(string_info('Capybara'))
print(string_info('Armageddon'))

# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь:
def is_contains(string, list_to_search):
    for i in range(1, len(list_to_search)):
        list_to_search_l = lower_string(list_to_search[i])
    if lower_string(string) in list_to_search_l:
        count_calls()
        return True
    else:
        count_calls()
        return False
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
