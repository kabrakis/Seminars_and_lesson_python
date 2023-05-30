# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

# num = []
# count = 0
# array = input('Введите цифры через пробел ').split()
# for i in range(len(array)):
#     array[i] = int(array[i])
#     num=array[i]
# print (count)

num = [1, -2, 3, -4, 5, 1]
count = 0
array = num[0]

for i in range(len(num)):
    if array != num[i]:
        count+=1
print (count+1)

# import random

# list_1 = list()

# for i in range(0, 10):
#     n = random.randint(-1, 10)
#     list_1.append(n)
# print(list_1)
# print(set(list_1))
# result = len(set(list_1))
# print(result)