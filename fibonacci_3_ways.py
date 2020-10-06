# 1 recursion
def fibonacci_rec(n):
    if n in [1, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 1 optimize recursion
from functools import lru_cache


@lru_cache(None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 2 memory safe mode
def fibonacci(n):
    a = 1
    b = 1
    if n <= 1:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


# 3 dynamic programing

FibArray = [1, 1]


def fibonacci_dyno(n):
    if n <= 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


fibonacci(70)  # 190392490709135)
fibonacci(60)  # 1548008755920
fibonacci(50)  # 12586269025)
