try:
    number = int(input("Введите целое положительное число: "))
    while number <= 0:
        print("Введите число больше нуля. Повторите ввод.")
        number = int(input("Введите целое положительное число: "))
    while number >= 0:
        print("Счетчик =", number)
        number -= 1
except ValueError:
    print("Вы ввели не число")
