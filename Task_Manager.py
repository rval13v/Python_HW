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

    def list_tasks(self): # Перечисляет все задачи 
        print(self)         

    def add_task(self, description: str):
        # Проверяем, нет ли такой задачи
        for task in self.tasks:
            if task["description"] == description:
                print("Такая задача уже существует.")
                return
        # Если задача уникальна, добавляем её
        self.tasks.append({"description": description, "completed": False})
        
    def complete_task(self, index: int):
        try:
            index = int(index)
            if 0 <= index < len(self.tasks):
                self.tasks[index]['completed'] = True
                print(f"Задача #{index} успешно отмечена как выполненная.")
            else:
                print("Задача с таким индексом не найдена.")
        except ValueError:
             print("Ошибка: Индекс должен быть целым числом.")
        except Exception as e:
            print(f"Ошибка: {e}")         

    def remove_task(self, index):
        try:
            index = int(index) 
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
                print(f"Задача #{index} удалена.")
            else:
                print("Задача с таким индексом не найдена.")
        except ValueError:
            print("Ошибка: Индекс должен быть целым числом.")
        except Exception as e:
            print(f"Ошибка: {e}")
      
    def save_to_json(self, filename: str):
        with open(filename, 'w') as file:
            try:
                json.dump(self.tasks, file, indent=4)  # indent=4 делает форматирование более читаемым        
            except json.JSONDecodeError as e:
                print(f"Ошибка при разборе JSON: {e}")
        
    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except json.JSONDecodeError as e:
            print(f"Ошибка при разборе JSON: {e}")


todo_list = TaskManager()


todo_list.add_task("Купить продукты")
todo_list.add_task("Сделать домашнюю работу")
todo_list.add_task("Ничего не делать")
todo_list.add_task("Сделать все")


menu = {
    "1": {"desc": "Показать все задачи", "func": todo_list.list_tasks},
    "2": {"desc": "Добавить новую задачу", "func": lambda: todo_list.add_task(input("Введите название задачи: "))},
    "3": {"desc": "Удалить задачу", "func": lambda: todo_list.remove_task(input("Введите номер задачи для удаления: "))},
    "4": {"desc": "Отметить задачу выполненной", "func": lambda: todo_list.complete_task(input("Введите номер выполненной задачи: "))},
    "5": {"desc": "Сохранить задачу в JSON", "func": lambda: todo_list.save_to_json("tasks.json.txt")},
    "6": {"desc": "Загрузить задачу из JSON", "func": lambda: todo_list.load_from_json("tasks.json.txt")}, 
    "0": {"desc": "Выход", "func": exit}
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
            action = menu[choice]['func']
            if callable(action):
                action()
        else:
            print("Неверный выбор. Повторите ввод.")

if __name__ == "__main__":
    main()
    
