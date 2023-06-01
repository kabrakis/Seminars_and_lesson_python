# Задача No27. Решение в группах
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore 
# The shells that she sells are sea shells 
# I'm sure.So if she sells sea shells on the sea shore I'm 
# sure that the shells are sea shore shells
# Output: 13

a = " She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
j= a.split()
b = ""
count=0
for c in j:
    if c not in b:
        print(f"{c}: {j.count(c)}")
        b += c
        count+=1
print(f"различных слов в тексте {count}")