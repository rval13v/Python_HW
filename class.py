class Task:
    def __init__(self, task, period, owner_task, status="Incomplete"): #Конструктор класса принимает четыре параметра: task (название задачи), period (количество дней),
    # owner_task (ответственный исполнитель) и статус (status)
        self.task = task # Внутри конструктора задаются свойства экземпляра класса. хранит название задачи.
        self.period = period # хранит срок выполнения в днях.
        self.owner_task = owner_task # хранит имя исполнителя.
        self.status = status # хранит статус задачи 

    def __str__(self): # Возвращает строку представления задачи.
        return f"Тask: {self.task}, Period: {self.period} days, Owner: {self.owner_task}, Status: {self.status}"
        
class ToDoList:
    def __init__(self):
        self.tasks = []   # пустой списк задач

    def __str__(self): #Переопределяет стандартный вывод объекта ToDoList
        result = ""
        for task in self.tasks:
            result += str(task) + "\n"
        return result.strip()
 
    def add_task(self,task):
        same_task = [same_task.task.lower() for same_task in self.tasks]
        if task.task.lower() in same_task:
            print(f"Такая задача уже существует")
            return
        self.tasks.append(task)

    def list_tasks(self): # Перечисляет все задачи 
        for task in self.tasks:
            print(task)    

    def remove_task(self, task_name): # Удаляем задачу по её названию. Метод remove_task принимает два аргумента:
# self ссылающийся на текущий экземпляр класса.
# task_name название задачи, которую нужно удалить.
        task_to_remove = input("Введите название задачи для удаления: ").strip()
        for task in self.tasks[:]:  # Проходим по копии списка, чтобы избежать проблем с изменением размера
            if task.task.lower() == task_name.lower(): #выполняется проверка на совпадение названий задач
                self.tasks.remove(task)
                print(f"Задача '{task_name}' успешно удалена.")
                return
        print(f"Задача '{task_name}' не найдена.")
            
    def complete_task(self, task_complete):
        task_to_complete = input("Введите название задачи которая выполнена: ").strip()
        for task in self.tasks[:]:  # Проходим по копии списка, чтобы избежать проблем с изменением размера
            if task.task.lower() == task_complete.lower(): #выполняется проверка на совпадение названий задач
                task.status = "Complete"
                print(f"Задача '{task_complete}' успешно выполнена.")
                return
            print(f"Задача '{task_complete}' не найдена.")
           
           
todoList = ToDoList()

todoList.add_task(Task("Разработка дизайна интерфейса", 7, "Иванов Иван"))
todoList.add_task(Task("Проведение тестирования нового функционала", 3, "Иванова Анна"))
todoList.add_task(Task("Создание прототипа веб-приложения", 10, "Петрова Мария"))  
todoList.add_task(Task("Организация новогоднего праздника", 15, "Сидоров Алексей"))         

menu = {
    "1": {"desc": "Показать все задачи", "func": todoList},
    "2": {"desc": "Удалить задачу", "func": todoList.remove_task},
    "3": {"desc": "Отметить задачу выполненной", "func": todoList.complete_task},
    "0": {"desc": "Выход", "func": None}
}


def main():
    while True:
        print("\nМеню:")
        for key, item in menu.items():
            print(f"{key}. {item['desc']}")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "0":
            print("Выход из программы.")
            break
        elif choice in menu:
            action = menu[choice]["func"]
            if action:
                action(main)
        else:
            print("Неверный выбор. Повторите ввод.")


if __name__ == "__main__":
    
    
    main()
