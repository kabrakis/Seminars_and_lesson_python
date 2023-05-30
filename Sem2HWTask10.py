# Задача 10
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

array = input('Введите цифру 1 если решка, введите 0 если орел ').split()
res = 0
count_orel = 0
count_reshka = 0
for i in range(len(array)):
    array[i] = int(array[i])
    if array[i] == 1:
        count_reshka += 1
    else:
        count_orel += 1
if count_orel > count_reshka:
    res = count_reshka
else:
    res = count_orel
print(f"орлов = {count_orel}, решек = {count_reshka}, минимальное количество монет которых нужно перевернуть = {res}")

