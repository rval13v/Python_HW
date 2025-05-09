def sum_lists(longer, shorter):
    result = [] # Создаем пустой список
    for i in range(len(shorter)):  # Складываем элементы по индексам
        result.append(shorter[i] + longer[i])

    start_index = len(shorter)
    result.extend(longer[start_index:])

    return result

def check_lists(numbers_1, numbers_2):
    longer = max(numbers_1, numbers_2, key=len)
    shorter = min(numbers_1, numbers_2, key=len)

    return sum_lists(longer, shorter)

numbers_1 = [1, 2, 3, 4, 7, 4, 5]
numbers_2 = [1, 2, 3, 3, 3, 7, 7, 6]

result = check_lists(numbers_1, numbers_2)
print(result)
