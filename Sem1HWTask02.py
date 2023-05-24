# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

from math import floor
number = int(input('введите трехзначное число: '))
if (number >= 100 and number <= 999):
    first_num = floor(number / 100)
    second_num = floor(number / 10) % 10
    third_num = floor(number % 10)
    print(
        f'Ваше число: {number}, а сумма его чисел: {first_num}+{second_num}+{third_num} = {first_num+second_num+third_num}')
else:
    print('Это число меньше или больше трехзначного')
