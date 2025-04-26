def cycle(input_text):
    punctuation = '''()-[]{};:"\\,<>./?@#$%^&*_~'''  # Создаётся строка punctuation,
    # содержащая все символы пунктуации, которые мы хотим удалить из текста.
    text_new = "".join(char for char in input_text if char not in punctuation) #Генератор перебирает каждый символ
    # в input_text. Если символ не в punctuation, он добавляется к новой строке text_new
    words = text_new.split() # Разбиваем очищенный текст на слова по пробелам, получаем список words
    longest_word = max(words, key=len) # Находим самое длинное слово в списке words, сравнивая длины слов.
    word_count = len(words) # Подсчитываем общее количество слов
    print("Words:", word_count)
    print("Longest word:", longest_word)
    return words


def vovels_sum(input_text):
    vovels = "аеёиоуыэюяaeiouy"
    count = 0 #Переменная count cчётчик гласных.
    for char in input_text: # Проходим по каждому символу оригинального текста (с учетом пунктуации).
    # Если символ — гласная, увеличиваем счётчик count.
        if char in vovels:
            count += 1
    print("Vowels:", count)


def counter(words):
    same = {} # Создаем пустой словарь
    for word in words: # Проходимся по каждому слову в списке words
        if word in same: # Если слово уже есть в словаре
            same[word] += 1 #Увеличиваем счетчик этого слова на 1
        else:
            same[word] = 1 # Если слова еще нет с словаре, добавляем его со знач.1
    sorted_values = sorted(same.items(), key=lambda tpl: tpl[1], reverse=True )
    # Сортируем элементы  словаря по значению tpl[1] в порядке убывания (reverse=True )
    return dict(sorted_values) # Возвращаем отсортированный словарь


input_text = str(input("Введите текст: ")).strip().lower() #strip() — удаляет пробелы в начале и в конце строки.
# lower() — переводит текст в нижний регистр (чтобы не различать слова по регистру)


words = cycle(input_text)
vovels_sum(input_text)
print("Word frequencies:", counter(words))


# Заметки
#"" - пустая строка
#.join() - метод добавления символа к строке
#char до начала цикла - то что метод в конечном счете будет добавлять в строку


