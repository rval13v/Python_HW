try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    message = '''
    Выберете математическую операцию:

    + : Сложение
    - : Вычитание
    / : Деление
    * : Умножение

    Ваш выбор:
    '''
    operation = input(message)

    if operation == '+':
        print('Сложение')
        result = num1 + num2
    elif operation == '-':
        print('Вычитание')
        result = num1 - num2
    elif operation == '/':
        print('Деление')
        result = num1 / num2
    elif operation == '*':
        print('Умножение')
        result = num1 * num2
    else:
        print('Неизвестная операция')

    print("Результат:", result)

except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
