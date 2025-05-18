def calculate_average(grades): # определение функции, которая будет рассчитывать ср.знач из списка grades
    if len(grades) == 0: # если список grades пустой, функция возвращает 0, чтобы избежать деления на 0
        return 0
    average = sum(grades) / len(grades) # считаем среднее
    return round(average, 2)


def add_student(name, grades): # функция создает студента по имени и списку баллов
    if not grades: # если баллы отсут, то raise
        raise ValueError("Нужно ввести хотя бы один балл.") # raise можно принудительно вызвать одно исключение
    return {"name": name, "grades": grades} # возвращает словарь, представляющий студента


def student_average(students): # информ о студенте
    print("\nТекущий список студентов:")
    for student in students: # перебирает всех студентов в списке
        avg = calculate_average(student["grades"]) # считает Средний балл
        if avg >= 75:
            status = "Успешен"
        else:
            status = "Неуспешен"
        print(f"\nСтудент: {student['name']}")
        print(f"Статус: {status}")
        print(f"Средний балл: {avg}")


def student_reduction(students):
    new_average = min(students, key=lambda s: calculate_average(s['grades'])) # находит студента с мин ср баллом
    students.remove(new_average) # удаляет студента
    print(f"Удален студент с самым низким средним баллом: {new_average['name']} ({calculate_average(new_average['grades'])})\n")


def overall_average(students): # общий Средний балл
    if not students:
        print("\nСтуденты отсутвуют")
        return
    total = sum(calculate_average(student["grades"]) for student in students)
    all_average = round(total / len(students), 2)
    print(f"\nОбщий средний балл всех студентов: {all_average}")


def update_list_students(students):
    print("\nОбновлённый список студентов:")
    for student in students:
        print(f"{student['name']}, Баллы: {student['grades']}, Средний балл: {calculate_average(student['grades'])}")


students = [
    {"name": "Harry", "grades": [90, 58, 76]},
    {"name": "Hermione", "grades": [90, 85, 86]},
    {"name": "Ron", "grades": [90, 68, 75]},
    {"name": "Draco", "grades": [70, 93, 74]}
]


student_average(students) # вызов текущий студентов и их Статус


input_text = input("\nВведите имя нового студента: ").strip()
grades = [] # пустой список для баллов в который вводим баллы 

print("Введите баллы (по одному). Чтобы закончить — нажмите Enter без ввода.")

while True: # бесконечный цикл ввожа оценок, пока не наступит break
    grade_input = input(f"Балл {len(grades) + 1}: ").strip() # выводит запрос баллов по очереди
    if grade_input == "": # если нажат пустой Enter
        break
    try:
        grade = int(grade_input)
        if 0 <= grade <= 100:   
            grades.append(grade)
        else:
            print("Балл должен быть от 0 до 100.")
    except ValueError:
        print("Ошибка! Введите число.")

try:
    students.append(add_student(input_text, grades))
except ValueError as e: # переменная в которую ловится Ошибка
    print(f"Ошибка: {e}")
else:
    student_reduction(students)

    
update_list_students(students)
overall_average(students)
