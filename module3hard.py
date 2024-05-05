def sum_int_str(a):
    if isinstance(a, int):
        return a
    else:
        return len(a)

def sum_dict(**a):  # print(sum_dict(**dict_))
    summa = 0
    for key, value in a.items():
        summa += sum_int_str(key) + sum_int_str(value)
    return summa

def sum_vector(a):
    summa = 0
    for i in range(len(a)):
        if isinstance(a[i], str) or isinstance(a[i], int):
            summa += sum_int_str(a[i])
        else:
            if isinstance(a[i], dict):
                summa += sum_dict(**a[i])
            else:
                if isinstance(a[i], set):
                    a[i] = list(a[i])
                    summa += sum_vector(a[i])
                else:
                    summa += sum_vector(a[i])
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(sum_vector(data_structure))
