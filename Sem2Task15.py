# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает 
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Далее N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9

n = int(input('введите n '))
kg = int(input('введите kg '))
max = kg
min = kg
for i in range(n-1):
    kg = int(input("введите вес арбуза: "))
    if kg > max:
        max = kg
    else:
        if kg<min:
            min = kg
print(f"маленький арбуз = {min} а большой = {max}")
