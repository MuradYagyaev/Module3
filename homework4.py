# Модуль 3 урок №4. "Распаковка параметров и параметры функции"
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Функция с параметрами по умолчанию:
print_params()              # Вывод: 1 строка True
print_params(b=25)          # Вывод: 1 25 True
print_params(c=[1, 2, 3])   # Вывод: 1 строка [1, 2, 3]

# Распаковка параметров:
values_list = ['текст', 7, False]
values_dict = {'a': True, 'b': 'Переменная', 'c': 11}
print_params(*values_list)      # Вывод: текст 7 False
print_params(**values_dict)     # Вывод: True Переменная 11

# Распаковка + отдельные параметры
values_list2 = ['текст', 2.5]
print_params(*values_list2, 15)     # Вывод: текст 2.5 15
