# import numpy as np

def return_codes():
    first_str = '79-800'.replace('-', '')
    second_str = '80-155'.replace('-', '')

    return [str(num)[:2:] + '-' + str(num)[2::] for num in range(int(first_str), int(second_str))]


print(return_codes())


def check_num(lst, n):
    return [num for num in range(1, n) if num not in lst]


print(check_num([2, 3, 7, 4, 9], 10))


def number_range():
    # without using numpy.arange
    start_num = 2
    lst = []
    while start_num <= 5.5:
        lst.append(start_num)
        start_num += 0.5

    return lst


print(number_range())

