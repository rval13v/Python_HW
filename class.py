class Task:
    def __init__(self, task, period, owner_task, status="Incomplete"): #Конструктор класса принимает четыре параметра: task (название задачи), period (количество дней),
    # owner_task (ответственный исполнитель) и статус (status), которое по умолчанию равно "Incomplete" («не выполнено»).
        self.task = task # Внутри конструктора задаются свойства экземпляра класса. хранит название задачи.
        self.period = period # хранит срок выполнения в днях.
        self.owner_task = owner_task # хранит имя исполнителя.
        self.status = status # хранит статус задачи 

    def __str__(self): # Возвращает красивую строку представления задачи.
        return f"Тask: {self.task}, Period: {self.period} days, Owner: {self.owner_task}, Status: {self.status}"
        
class ToDoList:
    def __init__(self):
        self.tasks = []   # пустой списк задач
 
    def add_task(self,task):
        self.tasks.append(task)

    def list_tasks(self): # Перечисляет все задачи 
        for task in self.tasks:
            print(task)    
    
    def __str__(self): #Переопределяет стандартный вывод объекта ToDoList
        result = ""
        for task in self.tasks:
            result += str(task) + "\n"
        return result.strip()
    
    def remove_task(self, task_name): # Удаляем задачу по её названию. Метод remove_task принимает два аргумента:
# self ссылающийся на текущий экземпляр класса.
# task_name название задачи, которую нужно удалить.
        
        for task in self.tasks[:]:  # Проходим по копии списка, чтобы избежать проблем с изменением размера
            if task.task.lower() == task_name.lower(): #выполняется проверка на совпадение названий задач
                self.tasks.remove(task)
                print(f"Задача '{task_name}' успешно удалена.")
                return
        print(f"Задача '{task_name}' не найдена.")
            
           
todoList = ToDoList()

todoList.add_task(Task("Разработка дизайна интерфейса", 7, "Иванов Иван", "Complete"))
todoList.add_task(Task("Проведение тестирования нового функционала", 3, "Иванова Анна", "Complete"))
todoList.add_task(Task("Создание прототипа веб-приложения", 10, "Петрова Мария", "Complete"))  
todoList.add_task(Task("Организация новогоднего праздника", 15, "Сидоров Алексей", "Complete"))         


print(todoList)

task_to_remove = input("Введите название задачи удаления: ").strip()
todoList.remove_task(task_to_remove)

print(todoList)

 
