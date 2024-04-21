# Модуль 3 урок №1. "Пространство имен и способы вызова функции"
a = 5
b = 6

def test():
    a = 15
    b = 17
    print('a =', a)
    print('b =', b)

def test2(parameter1='параметр1', parameter2='параметр2', parameter3='параметр3'):
    print(f'{parameter1}; {parameter2}; {parameter3}')


test()
test2()
test2(1, 2, 3)
test2(parameter2=24)
print(f'a = {a}; b = {b}')
