# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# def SimpleNum(num):
#     b=True
#     for i in range(2,num):
#         if num%i==0:
#             b=False
#     return b

# print("Enter num")
# n=int(input())
# print(SimpleNum(n))

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

# n = int(input("Введите число: "))
# if is_prime(n):
#     print(n, "является простым числом")
# else:
#     print(n, "не является простым числом")

# import math


# n = int(input("Введите число: "))

# def prNum(n):
#     for i in range(2, int(math.sqrt(n))):
#         if n % i == 0:
#             return print(f"Число {n} не является простым.")
#     return print(f"Число {n} простое.")

# prNum(n)