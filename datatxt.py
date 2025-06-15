def read_file(mode='r'):
    try:
        with open('data.txt', mode) as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файл не найден.")
    except PermissionError:
        print("Нет прав доступа к файлу.")
   
def read_lines_file(mode='r'):
    try:
        with open('data.txt', mode) as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Файл не найден.")
    except PermissionError:
        print("Нет прав доступа к файлу.")

def write_file(text, mode='a'):
    try:
        with open('data.txt', mode) as file:
            file.write(text + '\n')
            print("Данные успешно записаны в файл.")
    except FileNotFoundError:
        print("Файл не найден.")
    except PermissionError:
        print("Нет прав доступа к файлу.")

def copy_file(original_file, new_file):
    try:
        with open(original_file, 'rb') as org_f,\
            open(new_file, 'wb') as nw_f:
                nw_f.write(org_f.read())
    except FileNotFoundError:
        print("Исходный файл не найден.")
    except IOError:
        print("Ошибка при копировании файла.")
    except Exception as e:
        print("Возникла неизвестная ошибка: {e}")
                

read_file('r')
write_file("Новая запись.", 'a')
read_lines_file('r')
copy_file('data.txt', 'data_copy.txt')
