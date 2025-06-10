library = {
    "Преступление и наказание": {"author": "Фёдор Достоевский", "year": 1866, "availability": "n"},
    "Война и мир": {"author": "Лев Толстой", "year": 1869, "availability": "y"},
    "1984": {"author": "Джордж Оруэлл", "year": 1949, "availability": "y"},
    "Старик и море": {"author": "Эрнест Хемингуэй", "year": 1952, "availability": "y"},
    "Процесс": {"author": "Франц Кафка", "year": 1925, "availability": "y"},
    "Вишнёвый сад": {"author": "Антон Чехов", "year": 1904, "availability": "y"},
    "Код да Винчи": {"author": "Дэн Браун", "year": 2003, "availability": "y"},
    "Бойцовский клуб": {"author": "Чак Паланик", "year": 1996, "availability": "n"},
    "Азазель": {"author": "Борис Акунин", "year": 1998, "availability": "y"}

}

def book_list_view():
    for title, details in library.items():
        if details["availability"] == "y":
            status = "В наличии"
        elif details["availability"] is None:
            status = "Доступность неизвестна"
        else:
            status = "Нет в наличии"

        print(f"Книга: {title}\n\tАвтор: {details['author']},\n\tГод издания: {details['year']},\n\tСтатус: {status}\n")


def add_book():
    title = input("Введите название книги: ").strip()
    if not title:
        print("Ошибка: название книги не может быть пустым")
        return

    if title in library:
        print(f"Книга '{title}' уже есть в библиотеке.")
        choice = input("Обновить данные книги? Да/Нет [y/n]: ").strip().lower()
        while choice not in ['y', 'n']:
            choice = input("Ошибка ввода. Повторите выбор: Да/Нет [y/n]: ").strip().lower()
        if choice == 'n':
            print("Добавление книги отменено.")
            return
        else:
            print("Обновление данных книги.")
    else:
        print(f"Добавляем новую книгу '{title}'.")

    author = input("Введите автора книги: ").strip()
    if not author:
        print("Ошибка: автор книги не может быть пустым")
        return

    try:
        year = int(input("Введите год издания книги: "))
    except ValueError:
        print("Ошибка: год должен быть числом")
        return

    library[title] = {"author": author, "year": year, "availability": None}
    print(f"Книга '{title}' успешно добавлена или обновлена.")


    library[title] = {"author": author, "year": year, "availability": None}
    print(f"Книга '{title}' успешно добавлена.")
    return True


def remove_book():
    title = input("Введите название книги для удаления: ").strip()
    if title in library:
        del library[title]
        print(f"Книга '{title}' удалена из библиотеки")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.")


def issue_book():
    title = input("Введите название книги для выдачи: ").strip()
    if title in library:
        if library[title]["availability"] != "n":
            library[title]["availability"] = "n"
            print(f"Книга '{title}' выдана.")
        else:
            print(f"Книга '{title}' недоступна для выдачи.")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.")


def return_book():
    title = input("Введите название книги для возврата: ").strip()
    if title in library:
        if library[title]["availability"] == "n":
            library[title]["availability"] = "y"
            print(f"Книга '{title}' возвращена.")
        else:
            print(f"Книга '{title}' уже есть в библиотеке.")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.")


def find_book():
    title = input("Введите название книги для поиска: ").strip()
    if title in library:
        details = library[title]
        if details["availability"] == "y":
            status = "В наличии"
        elif details["availability"] is None:
            status = "Доступность неизвестна"
        else:
            status = "Нет в наличии"

        print(f"Книга: {title}\n\tАвтор: {details['author']},\n\tГод издания: {details['year']},\n\tСтатус: {status}\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.")


menu = {
    "1": {"desc": "Добавить книгу", "func": add_book},
    "2": {"desc": "Удалить книгу", "func": remove_book},
    "3": {"desc": "Выдать книгу", "func": issue_book},
    "4": {"desc": "Вернуть книгу", "func": return_book},
    "5": {"desc": "Найти книгу", "func": find_book},
    "6": {"desc": "Список книг", "func": book_list_view},
    "0": {"desc": "Выход", "func": None}
}


def main():
    while True:
        print("\nМеню:")
        for key, item in menu.items():
            print(f"{key}. {item['desc']}")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "0":
            print("Выход из программы.")
            break
        elif choice in menu:
            action = menu[choice]["func"]
            if action:
                action()
        else:
            print("Неверный выбор. Повторите ввод.")


main()






    



