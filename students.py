students = [
    {"name": "Harry", "grades": [90, 78, 76]},
    {"name": "Hermione", "grades": [90, 85, 86]},
    {"name": "Ron", "grades": [60, 68, 75]},
    {"name": "Draco", "grades": [70, 93, 74]}
]

def calculate_average(grades):
    if len(grades) == 0:
	    return 0
    average = sum(grades) / len(grades)
    return round(average, 2)

def new_student(students):
    students.append({"name": "Barry", "grades": [90, 43, 94]})
    return students


new_student(students)

def student_check(students):
    for student in students:       
        avg = calculate_average(student["grades"])
        if avg >= 75:
            status = "Успешен"
        else:
            status = "Неуспешен"
        
        print(f"Студент: {student['name']}\nСтатус: {status}")
        print(f"Средний балл у {student['name']}: {avg}\n")
  

student_check(students)

def student_del(students):
    
    std_udal = min(students, key=lambda s: calculate_average(s['grades']))
    students.remove(std_udal)
    print(f"Удален студент с самым низким средним баллом: {std_udal['name']} ({calculate_average(std_udal['grades'])})\n")


student_del(students)

all_avg = sum(calculate_average(student["grades"]) for student in students)
all_average = round(all_avg / len(students), 2)
print(f"Общий средний балл всех студентов: {all_average}")
