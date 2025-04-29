n = 100
even_numbers = [i for i in range(0, n + 1, 2)]
result = sum(even_numbers)
print(f"Сумма четных чисел от 0 до {n}: {result}")


x = 10
print("Квадраты нечетных чисел от 0 до", x)
squares = [i ** 2 for i in range(1, x + 1) if i % 2 != 0]
print(squares)


count = 0 # Создаем счетчик
while True:
    number = int(input("Введите число: "))
    if number > 0:
        count += 1 # Если число положительное, то увеличиваем счетчик на 1
    elif number < 0:
        print("Счетчик:", count)  # Выводим количество введенных положительных чисел
        break  # Прерываем цикл, когда введено отрицательное число
