# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*

# 385916 -> yes
# 123456 -> no

# import array as arr

# numbers = arr.array('i',[1,2,3,4,5,6])
# print(numbers)
# res_1=numbers[0]+numbers[1]+numbers[2]
# print (res_1)
# res_2=numbers[3]+numbers[4]+numbers[5]
# print (res_2)
# if res_1 == res_2:
#     print('yes')
# else:
#     print('no')

# len = int (input('введите длинну массива: '))
# array = [0]*len
# for i in range (len):
#     print ("array[",i,"]=")
#     array[i]=int(input())
# print(array)
# res_1=array[0]+array[1]+array[2]
# res_2=array[3]+array[4]+array[5]
# if res_1 == res_2:
#     print('yes')
# else:
#     print('no')

array = input('Введите цифры через пробел ').split()
for i in range(len(array)):
    array[i] = int(array[i])
res_1=array[0]+array[1]+array[2]
res_2=array[3]+array[4]+array[5]
if res_1 == res_2:
       
       print(f'Ваш билет счастливый')
else:
    print(f'Ваш билет не счастливый')