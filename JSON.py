ToDoList = [
    {"description": "Задача_1", "status": "Completed"},
    {"description": "Задача_2", "status": "Completed"},
    {"description": "Задача_3", "status": "Completed"},
    {"description": "Задача_4", "status": "Completed"}
]

class Task:
    def __init__(self, description, status=False): 
        self.description = description # Внутри конструктора задаются свойства экземпляра класса. хранит название задачи.
        self.status = status # хранит срок выполнения в днях.

    def __str__(self): # Возвращает строку представления задачи.
        return f"description: {self.description}, Status: {self.status}"    

class ToDoList:
    def __init__(self):
        self.descriptions = []   # пустой списк зад 
        
    def __str__(self): #Переопределяет стандартный вывод объекта ToDoList
        result = ""
        for description in self.descriptions:
            result += str(description) + "\n"
        return result.strip()
        
    def add_task(self, description: str):
        same_description = [same_description.description.lower() for same_description in self.descriptions]
        if description.description.lower() in same_description:
            print(f"Такая задача уже существует")
            return
        self.tasks.append(description)        
    
