def sum_lists(longer, shorter):
    result = [] # Создаем пустой список
    for i in range(len(shorter)):  # Складываем элементы по индексам
        result.append(shorter[i] + longer[i])

    for i in range(len(shorter), len(longer)):  # Добавляем оставшиеся элементы длинного списка
        result.append(longer[i])

    return result

def check_lists(numbers_1, numbers_2):
    if len(numbers_1) > len(numbers_2):  # Сравниваем длину
        longer = numbers_1
        shorter = numbers_2
    else:
        longer = numbers_2
        shorter = numbers_1

    return sum_lists(longer, shorter)

numbers_1 = [1, 2, 3, 4, 7, 4, 5]
numbers_2 = [1, 2, 3, 3, 3, 7, 7, 6]

result = check_lists(numbers_1, numbers_2)
print(result)
