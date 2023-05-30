# Задача No21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input:
# [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#  {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит



data = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

unique_values = set()

for item in data:
    for value in item.values():
        unique_values.add(value.strip())  # Добавляем уникальные значения в множество

print(list(unique_values))
