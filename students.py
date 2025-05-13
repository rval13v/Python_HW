students = [
    {"name": "Harry", "grades": [90, 78, 76]},
    {"name": "Hermione", "grades": [90, 85, 86]},
    {"name": "Ron", "grades": [60, 61, 75]},
    {"name": "Draco", "grades": [70, 43, 74]}
]

def calculate_average(grades):
    average = sum(grades) / len(grades)
    return round (average, 2)

def new_student(students):
    students.append({"name": "Barry", "grades": [90, 43, 94]})

def average_students(students):
    all_avg = 0
    for student in students:
        avg = calculate_average(student["grades"])
        if avg >= 75:
            print(f"Студент: {student['name']}\nСтатус: Успешен")
        else:
            print(f"Студент: {student['name']}\nСтатус: Неуспешен")
        print(f"Средний балл у {student['name']}: {avg}\n")
        all_avg += avg
    return all_avg


all_avg = average_students(students)


def del_stud(students):
    student_del = min(students, key=lambda s: calculate_average(s['grades']))
    students.remove(student_del)
    print(f"Удален студент с самым низким средним баллом: {student_del['name']} ({calculate_average(student_del['grades'])})\n")


def all_aver(students):
    all_average = round(all_avg / len(students), 2)
    print(f"Общий средний бал {all_average}")
    return all_average


new_student(students)
average_students(students)
del_stud(students)
all_aver(students)
