def max_number(a, b):
    if a >= b:
        return a
    else:
        return b


def autotest_max_number(a, b):
    assert max_number(3, 2) == 3, "Ошибка: большее число должно быть 3"
    assert max_number(-1, 1) == 1, "Ошибка: большее число должно быть 1"
    assert max_number(0, 0) == 0, "Ошибка: оба числа равны 0"
    assert max_number(-5, -6) == -5, "Ошибка: большее число должно быть -5"
print("Тест пройден")


def empty_function():
    pass


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

try:
    input_user = int(input("Введите число "))
    for i in even_numbers(input_user):
        print(i)
except ValueError:
    print("Введено не число!")
finally:
    print("Программа завершена")



