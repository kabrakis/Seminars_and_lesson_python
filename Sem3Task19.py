# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2 Output: [4, 5, 1, 2, 3]

# import random
# print("Enter num")
# num=int(input())
# arr.clear()
# for i in range(num):
#     arr.append(rand.randint(0,10))

# print("Enter k")
# k=int(input())
# print(arr)
# arr2=arr[:len(arr)-k]
# arr3=arr[len(arr)-k:]
# arr3.append(arr2)
# print(arr3)

# list_1 = []
# length = int(input('Enter length of list > '))
# k = int(input('k = '))
# for i in  range(length):
#     list_1.append(int(input()))

# print(list_1)

# for i in range(k):
#     tmp = list_1[-1]
#     list_1.insert(0, tmp)
#     list_1.pop()

# print(list_1)

# import random
# list_1 = list()
# for i in range(0, 10):
#     n = random.randint(0, 10)
#     list_1.append(n)

# print(list_1)

# step = int(input())

# result_list = list_1.copy()

# for i in range(step):
#     result_list.insert(0, result_list.pop())
# print(result_list)

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k - 1):
#     list.insert(0, list.pop())
# print(list)

# arr = [1, 2, 3, 4, 5]
# k = int(input())
# for i in range(k):
#     elem = arr.pop()
#     arr.insert(0, elem)

# print(arr)