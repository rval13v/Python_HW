import unittest
from Task_Manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def test_remove_task(self):
        todo_list = TaskManager()
        todo_list.add_task("Купить продукты")
        self.assertEqual(len(todo_list.tasks), 1)  # Проверяем, что задача добавлена
        
       
        todo_list.remove_task(0)
        self.assertEqual(len(todo_list.tasks), 0)
        self.assertNotIn("Купить продукты", [task['description'] for task in todo_list.tasks])

    def test_add_task(self):
        todo_list = TaskManager()
        todo_list.add_task("Купить пиво")         
        self.assertEqual(len(todo_list.tasks), 1)  # Проверяем, что задача добавлена
        
        
        todo_list.add_task(0)
        self.assertIn("Купить пиво", [task['description'] for task in todo_list.tasks])
        
)
        
if __name__ == '__main__':
    unittest.main()
