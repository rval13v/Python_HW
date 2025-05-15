def calculate_average(grades):
    if len(grades) == 0:
        return 0
    average = sum(grades) / len(grades)
    return round(average, 2)

def add_student():
    student_name = input("Введите имя студента: ")
    grades = []
    count_grades = 3
    while count_grades:
        try:
            grade = int(input("Введите балл: "))
            if 0 <= grade <= 100:
                grades.append(grade)
                count_grades -= 1
            else:
                print("Введите балл от 0 до 100")
        except ValueError:
            print("Ошибка! Введите балл от 0 до 100!")
            student = dict(name=student, grades=grade)
    return student

def student_average(students):
    for student in students:
        avg = calculate_average(student["grades"])
        if avg >= 75:
            status = "Успешен"
        else:
            status = "Неуспешен"

        print(f"Студент: {student['name']}\nСтатус: {status}")
        print(f"Средний балл у {student['name']}: {avg}\n")

def student_reduction(students):
    new_average = min(students, key=lambda s: calculate_average(s['grades']))
    students.remove(new_average)
    print(f"Удален студент с самым низким средним баллом: {new_average['name']} ({calculate_average(new_average['grades'])})\n")
 
def overall_average(students):
    total = 0
    for student in students:
        total += calculate_average(student["grades"])
    all_average = round(total / len(students), 2)
    print(f"Общий средний балл всех студентов: {all_average}")

students = [
    {"name": "Harry", "grades": [90, 58, 76]},
    {"name": "Hermione", "grades": [90, 85, 86]},
    {"name": "Ron", "grades": [60, 68, 75]},
    {"name": "Draco", "grades": [70, 93, 74]}
]


student_average(students)
students.append(add_student())
student_reduction(students)
overall_average(students)
