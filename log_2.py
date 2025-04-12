try:
    number = int(input("Введите целое число от 1  до 5: "))

    if number == 1:
        print('one')
    elif number == 2:
        print('two')
    elif number == 3:
        print('three')
    elif number == 4:
        print('four')
    elif number == 5:
        print('five')
    else:
        print('Введите целое число в диапазоне от 1  до 5!')
except ValueError:
    print("Ошибка: введите корректное целое число!")
finally:
    print("Программа завершена")