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

while True:
    title = input("Введите название книги: ").strip().lower()
    if not title:
        break

    if check_book(title):
        author = input("Введите автора книги: ").strip()
        while not author:
            author = input("Имя автора обязательно. Пожалуйста, повторите ввод: ").strip()
            
        try:
            year = int(input("Введите год издания книги: "))
            if add_book(title, author, year):
                pass
        except ValueError:
            print("Ошибка: год должен быть числом")

print("\nСписок книг в бибилиотеке: ")
book_list_view(library)
