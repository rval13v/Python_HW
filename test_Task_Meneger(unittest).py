import unittest
import json
import os

from Task_Manager import TaskManager

class TestTaskManager(unittest.TestCase):
    test_filename = "tasks.json.txt"

    def setUp(self):
        self.todo_list = TaskManager()

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
        self.assertIn("Купить пиво", [task['description'] for task in todo_list.tasks])
        
    def test_complete_task(self):
        self.todo_list.add_task("Купить пиво")
        self.todo_list.complete_task(0)
        self.assertTrue(self.todo_list.tasks[0]['completed'])  

    def tearDown(self):
        try:
            import os
            os.remove(self.test_filename)
        except OSError:
            pass

    def test_save_and_load_json(self):
        self.todo_list.add_task("Купить пиво")
        self.todo_list.save_to_json(self.test_filename)

        new_todo_list = TaskManager()
        new_todo_list.load_from_json(self.test_filename)

        self.assertEqual(new_todo_list.tasks, self.todo_list.tasks)
        

if __name__ == '__main__':
    unittest.main()
