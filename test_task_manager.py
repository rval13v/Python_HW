import pytest

from Task_Manager import TaskManager

@pytest.fixture
def todo_list():
    return TaskManager()

def test_remove_task(todo_list):
    todo_list.add_task("Купить продукты")
    assert len(todo_list.tasks) == 1  # Проверяем, что задача добавлена
    
    todo_list.remove_task(0)
    assert len(todo_list.tasks) == 0
    assert "Купить продукты" not in [task["description"] for task in todo_list.tasks]

def test_add_task(todo_list):
    todo_list.add_task("Купить пиво")
    assert len(todo_list.tasks) == 1  # Проверяем, что задача добавлена
