from abc import ABC, abstractmethod
import json
import logging
from typing import List

# Налаштування логування (без цього logging.info/error не виведуться в консоль)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class TaskSafe(ABC):

    @abstractmethod
    def completed_task(self) -> None:
        """Абстрактний метод для відмітки завдання як виконаного."""
        pass


class Task(TaskSafe):

    def __init__(self, title: str) -> None:
        # Перевірка типу на етапі створення об'єкта
        if not isinstance(title, str) or not title.strip():
            logging.error("Назва завдання повинна бути непустим рядком!")
            raise ValueError("Title must be a non-empty string")

        self.title = title
        self._is_completed = False
        logging.info(f"Створено завдання: '{self.title}'")

    def completed_task(self) -> None:
        """Переводить статус завдання у виконано."""
        self._is_completed = True
        logging.info(f"Завдання '{self.title}' виконано.")

    def get_status(self) -> str:
        """Повертає текстовий статус завдання."""
        status = "Виконано" if self._is_completed else "В процесі"
        return f"{self.title} [{status}]"

    def to_dict(self) -> dict:
        """Конвертує об'єкт завдання у словник для JSON."""
        return {"title": self.title, "is_completed": self._is_completed}


class ToList:

    def __init__(self) -> None:
        self._my_tasks: List[Task] = []

    def add_task(self, title: str) -> None:
        """Створення об'єкта Task всередині списку."""
        try:
            task = Task(title)
            self._my_tasks.append(task)
        except ValueError:
            print("Не вдалося додати завдання через помилку валідації.")

    def show_all(self) -> None:
        """Виводить усі завдання."""
        if not self._my_tasks:
            print("Список порожній.")
            return

        for index, task in enumerate(self._my_tasks, 1):
            print(f"{index}. {task.get_status()}")

    def get_tasks(self) -> List[Task]:
        return self._my_tasks


class JsonConverter:
    """Клас для конвертації списку завдань у JSON формат."""

    @staticmethod
    def to_json(to_list_obj: ToList) -> str:
        tasks_data = [task.to_dict() for task in to_list_obj.get_tasks()]
        # ensure_ascii=False потрібен для коректного відображення кирилиці
        return json.dumps(tasks_data, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # Створюємо менеджер завдань
    todo_list = ToList()

    # Додаємо завдання
    todo_list.add_task("Вивчити базовий синтаксис Python")
    todo_list.add_task("Розібратися з ООП та абстрактними класами")

    # Відмітимо перше завдання як виконане
    all_tasks = todo_list.get_tasks()
    if all_tasks:
        all_tasks[0].completed_task()

    print("\n--- Список завдань ---")
    todo_list.show_all()

    print("\n--- Конвертація в JSON ---")
    json_result = JsonConverter.to_json(todo_list)
    print(json_result)




    







    





    