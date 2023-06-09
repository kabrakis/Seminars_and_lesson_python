# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для 
# разных объектов отличается - то False. Для пустого набора объектов, 
# функция должна возвращать True. Аргумент characteristic - это функция, 
# которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same 
# if same_by(lambda x: x % 2, values):
# print(‘same’) else:
# print(‘different’)

values = [0, 2, 10, 6]  

def same_by(predicat, values):
   res = list(map(predicat, values))
   for i in range(1,len(res)):
       if res[i-1] != res[i]:
           return False
   return True
      
if same_by(lambda x: x % 2, values):
    print('same') 
else:
    print('different')