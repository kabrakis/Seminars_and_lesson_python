
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while


# Input:       5

# Output:    120
n = int (input('введите N '))
i=1
res = 1
if n>0:
    while i < n:
        i+=1
        res*=i
    print (res)
else:
    print("не надо так")