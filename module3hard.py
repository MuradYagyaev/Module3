# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Пока пришел к такому решению.

# Функция для расчета суммы чисел или длин строк, если элемент не вектор
def sum_dig_str(a):
    if isinstance(a, (int, float)):
        return a
    elif isinstance(a, str):
        return len(a)
    else:
        return 0

# Функция для расчета суммы длин строк и чисел, если элемент словарь
def sum_dict(**a):  # print(sum_dict(**dict_))
    summa = 0
    for key, value in a.items():
        summa += sum_dig_str(key) + sum_dig_str(value)
    return summa

# Основная функция с рекурсией для раскрытия вектора
def sum_array(a):
    summa = 0
    for i in range(len(a)):
        if isinstance(a[i], (list, tuple)):
            summa += sum_array(a[i])
        elif isinstance(a[i], set):
            a[i] = list(a[i])
            summa += sum_array(a[i])
        elif isinstance(a[i], dict):
            summa += sum_dict(**a[i])
        else:
            summa += sum_dig_str(a[i])
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


print(sum_array(data_structure))
