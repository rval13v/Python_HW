def calculate_average(grades):
    if len(grades) == 0:
        return 0
    average = sum(grades) / len(grades)
    return round(average, 2)


def add_student(name, grades):
    if not grades:
        raise ValueError("Нужно ввести хотя бы один балл.") # raise можно принудительно вызвать одно исключение
    return {"name": name, "grades": grades}


def student_average(students):
    print("\nТекущий список студентов:")
    for student in students:
        avg = calculate_average(student["grades"])
        if avg >= 75:
            status = "Успешен"
        else:
            status = "Неуспешен"
        print(f"\nСтудент: {student['name']}")
        print(f"Статус: {status}")
        print(f"Средний балл: {avg}")


def student_reduction(students):
    new_average = min(students, key=lambda s: calculate_average(s['grades']))
    students.remove(new_average)
    print(f"Удален студент с самым низким средним баллом: {new_average['name']} ({calculate_average(new_average['grades'])})\n")


def overall_average(students):
    total = 0
    for student in students:
        total += calculate_average(student["grades"])
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


student_average(students)


input_text = input("\nВведите имя нового студента: ").strip()
grades = []

print("Введите баллы (по одному). Чтобы закончить — нажмите Enter без ввода.")

while True:
    grade_input = input(f"Балл {len(grades) + 1}: ").strip()
    if grade_input == "":
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
except ValueError as e:
    print(f"Ошибка: {e}")
else:
    student_reduction(students)

    
update_list_students(students)
overall_average(students)
