# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()


a = input("введите что-то ")
b = ""
for c in a:
    if c not in b:
        print(f"{c}: {a.count(c)}")
        b += c

# s = 'a a a b c a a d c d d'
# s = s.split()
# print(s)
# final_string = ''
# for i in range(len(s)):
#     if s[0:i].count(s[i]) == 0:
#         final_string += f' {s[i]}'
#     else:
#         final_string += f' {s[i]}_{s[0:i].count(s[i])}'
# print(final_string)

# st = list(input("Введите строку: "))
# print(st)
# d = {}
# p = ""
# for i in range(len(st)):
#     if d.get(st[i]) != None:
#         d[st[i]] = int(d[st[i]])+1
#     else:
#         d[st[i]] = 1
#     p = p + f"{st[i]}_{d[st[i]]}"
# print(p)