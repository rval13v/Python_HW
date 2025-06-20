import json

class TaskManager:

    def __init__(self):
        self.tasks = []  # Пустой список задач
    
    def __str__(self):
        if not self.tasks:
            return "Список задач пуст."
        result = ""
        for index, task in enumerate(self.tasks):
            status = "завершена" if task["completed"] else "активна"
            result += f"#{index}: {task['description']}, {status}\n"
        return result.strip()

    def add_task(self, description: str):
        # Проверяем, нет ли такой задачи
        for task in self.tasks:
            if task["description"] == description:
                print("Такая задача уже существует.")
                return
        # Если задача уникальна, добавляем её
        self.tasks.append({"description": description, "completed": False})
        
    def complete_task(self, index: int):
        # Проверяем, существует ли задача с указанным индексом
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            print(f"Задача #{index} успешно отмечена как выполненная.")
        else:
            print("Задача с таким индексом не найдена.")

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]       
            print(f"Задача #{index} удалена.")
        else:
            print("Задача с таким индексом не найдена.")  

    def save_to_json(self, filename: str):
        with open(filename, 'w') as file:
            try:
                json.dump(self.tasks, file, indent=4)  # indent=4 делает форматирование более читаемым        
            except json.JSONDecodeError as e:
                print(f"Ошибка при разборе JSON: {e}")
        
    def load_from_json(self, filename: str):
        with open(filename, 'r') as file:
            try:
                self.tasks = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Ошибка при разборе JSON: {e}")


todo_list = TaskManager()


todo_list.add_task("Купить продукты")
todo_list.add_task("Сделать домашнюю работу")
todo_list.add_task("Ничего не делать")
todo_list.add_task("Сделать все")


print(todo_list)


todo_list.complete_task(1)  
todo_list.remove_task(3)


print(todo_list)


todo_list.save_to_json("tasks.json.txt")
print("Задачи сохранены в файл tasks.json")

todo_list.load_from_json("tasks.json.txt")
print("Задачи загружены из файла tasks.json")
