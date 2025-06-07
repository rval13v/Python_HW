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


def book_list_view(library):
    for title, details in library.items():
        if details["availability"] == "y":
            status = "В наличии"
        elif details["availability"] is None:
            status = "Доступность неизвестна"
        else:
            status = "Нет в наличии"

        print(f"Книга: {title}\n\tАвтор: {details['author']},\n\tГод издания: {details['year']},\n\tСтатус: {status}\n")


def add_book(title, author, year):
    if not title.strip() or not author.strip() or not year:
        print("Вы ничего не ввели, добавление пропущено")
        return False

    library[title] = {"author": author, "year": year, "availability": None}
    print(f"Книга '{title}' успешно добавлена.")
    return True


def check_book(title):
    if title in library:
        print(f"Предупреждение: Книга '{title}' уже присутствует в библиотеке.")
        choice = input("Обновить данные книги? Да/Нет [y/n]: ").strip().lower()
        while choice not in ['y', 'n']:
            choice = input("Ошибка ввода. Повторите выбор: Да/Нет [y/n]: ").strip().lower()
        return choice == 'y'
    else:
        print(f"Книга '{title}' не найдена в библиотеке. Она будет добавлена.")
        return True


def remove_book(title):
    if title in library:
        del library[title]
        print(f"Книга '{title}' удалена из библиотеки")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.")
 

def issue_book(title):
    if title in library:
        if library[title]["availability"] == "y" or library[title]["availability"] is None:
            library[title]["availability"] = "n"
            print(f"Книга '{title}' выдана.")
        else:
            print(f"Книга '{title}' недоступна для выдачи.")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.")


def return_book(title):
    if title in library:
        if library[title]["availability"] == "n":
            library[title]["availability"] = "y"
            print(f"Книга '{title}' возвращена.")
        else:
            print(f"Книга '{title}' уже есть в библиотеке.")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.")
        
        
title = input("Введите название книги: ").strip()
author = input("Введите автора книги: ").strip()


try:
    year = int(input("Введите год издания книги: "))
except ValueError:
    print("Ошибка: год должен быть числом")
else:
    if len(title) == 0 or len(author) == 0:
        print("Ошибка: поля не заполнены")
    else:
        if check_book(title):
            add_book(title, author, year)




print("\nСписок книг в библиотеке:")
book_list_view(library)


title_to_remove = input("Введите название книги для удаления: ").strip()
remove_book(title_to_remove)


title_to_issue = input("Введите название книги для выдачи: ").strip()
issue_book(title_to_issue)

title_to_return = input("Введите название книги для возврата: ").strip()
return_book(title_to_return)


print("\nОбновленный список книг в библиотеке:")
book_list_view(library)
