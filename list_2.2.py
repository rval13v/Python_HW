numbers_1 = [1, 2, 3, 4, 7, 4, 5]
numbers_2 = [1, 2, 3, 3, 3, 7, 7, 6]

if len(numbers_1) > len(numbers_2):  # Сравниваем длину
    longer = numbers_1
    shorter = numbers_2
elif len(numbers_1) < len(numbers_2):
    longer = numbers_2
    shorter = numbers_1
else:
    longer = numbers_1  # Если длины равны.
    shorter = numbers_2

result = []

def sum_lists():
    for i in range(len(shorter)):  # Индексы по длине короткого списка
        result.append(shorter[i] + longer[i])  # Складываем по индексам
    for i in range(len(shorter), len(longer)):
        result.append(longer[i])  # Добавляем остаток из длинного списка

    print(result)

sum_lists()