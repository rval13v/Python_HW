def calculate_average(grades):
    if not grades:
        return 0
    return round(sum(grades) / len(grades), 2)


def add_student(name):
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

    if not grades:
        print("Не введено ни одного балла. Студент не будет добавлен.")
        return None

    return {"name": name, "grades": grades}


def student_average(students):
    for student in students:
        avg = calculate_average(student["grades"])
        if avg >= 75:
            status = "Успешен"
        else:
            status = "Неуспешен"
        print(f"\nСтудент: {student['name']}, \n\tСтатус: {status} \n\tСредний балл: {avg}")


def student_reduction(students):
    if not students:
        return
    new_average = min(students, key=lambda s: calculate_average(s['grades']))
    students.remove(new_average)
    print(f"\nУдален студент с самым низким средним баллом: {new_average['name']} ({calculate_average(new_average['grades'])})")


def overall_average(students):
    if not students:
        print("\nСтуденты отсутствуют")
        return
    
    total = [grade for student in students for grade in student["grades"]]
    all_average = calculate_average(total)
    print(f"\nОбщий средний балл всех студентов: {all_average}")



students = [
    {"name": "Harry", "grades": [90, 98, 76]},
    {"name": "Hermione", "grades": [90, 85, 86]},
    {"name": "Ron", "grades": [90, 68, 75]},
    {"name": "Draco", "grades": [90, 93, 74]}
]

print("\nТекущий список студентов:")
student_average(students)


input_text = input("\nВведите имя нового студента: ").strip() # Ввод нового студента
if input_text:
    new_student = add_student(input_text)
    if new_student:
        students.append(new_student)
        print(f"\nДобавлен студент: {new_student['name']}")
else:
    print("Имя не введено. Добавление пропущено.")


student_reduction(students) # Удаление студента с самым низким средним баллом


print("\nОбновленный список студентов:")
student_average(students)
overall_average(students)
