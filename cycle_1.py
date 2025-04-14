while True:
    try:
        number = int(input("Введите целое  положительное число: "))
        if number < 0:
            print("Вы ввели отрицательное число. Повторите ввод.")
            continue
        elif number == 0:
            print("Введите число больше нуля.")
            continue

        while number != -1:
            print("Счетчик =", number)
            number -= 1
        break
    except ValueError:
        print("Введите целое положительное число")