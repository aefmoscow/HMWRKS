def test_function():
    print('Test function')

    def inner_function(*args):
        print('Я в области видимости функции test_function', *args)

    inner_function(5, 6)


test_function()
inner_function(8, 9)  # тут не работает
