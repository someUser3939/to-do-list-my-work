from typing import List
import logging
from abc import ABC, abstractmethod
import json



logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class TaskShablon(ABC):
    @abstractmethod
    def work_with_task():
        pass

class Task(TaskShablon):
    def __init__(self, operation: str, things: List = None ) -> None:
        self.operation = operation
        self.things = things if things is not None else
        logging.info(f'cnворення завдання та операций с ним {self.operation}')

    def work_with_task(self):
        print(
            f"виконали операцію {self.operation}, над елементами {self.things}"
        )
    def to_dict(self):
        return {"operation": self.operation, "things": self.things}


class Results:
    def __init__(self, filename: str = "todo_list.json") -> None:
        self.filename = filename

    def save_tasks(self, tasks: List[Task]) -> None:
        """Приймає список об'єктів Task і зберігає їх у JSON-файл"""
        try:
            # Перетворюємо список об'єктів у список словників
            data_to_save = [task.to_dict() for task in tasks]

            # Записуємо у файл (ensure_ascii=False дозволяє зберігати кирилицю коректно)
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data_to_save, file, ensure_ascii=False, indent=4)

            logging.info(f"Успішно збережено {len(tasks)} завдань у {self.filename}")
        except Exception as e:
            logging.error(f"Помилка при збереженні у файл: {e}")

    def load_tasks(self) -> List[dict]:
        """Завантажує дані з JSON-файлу"""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            logging.warning(f"Файл {self.filename} не знайдено. Повертаємо порожній список.")
            return 
        except Exception as e:
            logging.error(f"Помилка при читанні файлу: {e}")
            return



    





    