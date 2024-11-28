calls = 0 # Все эти значения должны быть в общем месте, для того,

# Чтобы можно было быстрее считывать работу вашего кода.

def count_calls():
    global calls
    calls += 1

def lower_string(elem): #Бесполезная функция, вы можете сделать преобразование в основной функции,

# А так вы просто забрали у себя время на написание данной конструкции.

    a = elem.lower()

return a

def string_info(string):
    count_calls()
    return f'({len(string)}, {string.upper()}, {string.lower()})' # F- строка вам тут не нужна, вам нужно вернуть кортеж
# А вы возвращаете строку

print(f'Для наглядности {type(string_info("Capybara"))}') # Все эти значения должны быть в общем месте, для того,

# Чтобы можно было быстрее считывать работу вашего кода.

print(string_info('Capybara')) # Все эти значения должны быть в общем месте, для того,

# Чтобы можно было быстрее считывать работу вашего кода.

print(string_info('Armageddon')) # Все эти значения должны быть в общем месте, для того,

# Чтобы можно было быстрее считывать работу вашего кода.

def is_contains(string, list_to_search):

    for i in range(1, len(list_to_search)): # Для чего перебирать по индексам, если можно перебирать сразу элементы?

# Если перебирать элементы, то переменную i нужно переименовать в elem

list_to_search_l = lower_string(list_to_search[i]) #Тогда вы сможете избавиться от этой строки

if lower_string(string) in list_to_search_l: # Ну а далее уже нужно будет просто подредактировать код

count_calls() #Для чего нам 2 раза писать одинаковую строку кода, если мы можем засунуть её в самое начало

# Вашей функции is_contains - 1 раз

return True

else:

count_calls() #Для чего нам 2 раза писать одинаковую строку кода, если мы можем засунуть её в самое начало

# Вашей функции is_contains - 1 раз

return False



# ВОТ В ЭТО МЕСТО МЫ ВСЁ ПЕРЕНОСИМ, ЧТОБЫ МОЖНО БЫЛО ОТСЛЕДИТЬ ПОРЯДОК ВЫПОЛНЕНИЯ ВСЕХ ФУНКЦИЙ И ЗНАЧЕНИЙ

# КОТОРЫЕ ТУДА ПЕРЕДАЮТСЯ

calls = 0

print(f'Для наглядности {type(string_info("Capybara"))}')

print(string_info('Capybara'))

print(string_info('Armageddon'))



print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches



print(calls)