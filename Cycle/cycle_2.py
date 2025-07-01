password = "123456"
while True:
    input_pass = input("Введите пароль: ")
    if input_pass != password:
        print("Вы ввели неправильный пароль. Повторите ввод.")
    elif input_pass == password:
        print("Добро пожаловать в систему!")
        break














