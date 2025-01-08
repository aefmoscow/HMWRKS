def custom_write(file_name, strings):
    strings_positions = 0
    dict_strings = {}
    file = open(file_name, 'w', encoding='utf-8')

    for inwrite_string in strings:
        strings_positions += 1
        byte = file.tell()
        dict_strings[(strings_positions, byte)] = inwrite_string
        # как сделать присвоение inwrite_string раньше не вижу, подглядел такой вариант
        file.write(inwrite_string + '\n')
    file.close()
    return dict_strings


# Пример  выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
