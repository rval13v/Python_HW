def book_list_view(library):
    for title, details in library.items():
        if details["availability"] == "y":
            status = "В наличии"
        else:
            status = "Нет в наличии"
        
        print(f"Книга: {title}\n\tАвтор: {details['author']},\n\tГод издания: {details['year']},\n\tСтатус: {status}\n")

library = {
    "Преступление и наказание": {
        "author": "Фёдор Достоевский",
        "year": 1866,
        "availability": "n"
    },
    "Война и мир": {
        "author": "Лев Толстой",
        "year": 1869,
        "availability": "y"
    },
    "1984": {
        "author": "Джордж Оруэлл",
        "year": 1949,
        "availability": "y"
    },
    "Старик и море": {
        "author": "Эрнест Хемингуэй",
        "year": 1952,
        "availability": "y"
    },
    "Процесс": {
        "author": "Франц Кафка",
        "year": 1925,
        "availability": "y"
    },
    "Вишнёвый сад": {
        "author": "Антон Чехов",
        "year": 1904,
        "availability": "y"
    },
    "Код да Винчи": {
        "author": "Дэн Браун",
        "year": 2003,
        "availability": "y"
    },
    "Бойцовский клуб": {
        "author": "Чак Паланик",
        "year": 1996,
        "availability": "n"
    },
    "Азазель": {
        "author": "Борис Акунин",
        "year": 1998,
        "availability": "y"
    }
}

book_list_view(library)


    
