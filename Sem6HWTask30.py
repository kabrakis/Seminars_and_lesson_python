# '''Задача 30: 
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_elm = int(input('Введите первый эл-т ')) 
diff = int(input('введите разность '))
size =int(input('Введите колл-во эл-ов '))
for i in range(size):
    print(first_elm + i * diff, end=' ')