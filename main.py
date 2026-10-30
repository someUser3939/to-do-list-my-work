"""
програма to-do-list
"""
from typing import List
import logging
from abc import ABC, abstractmethod
class TaskShablon(ABC):
    @abstractmethod
    def __init__(self, list: List=[0], operation) -> None:
        self.list = list
        self.operation = operation
        logging.info('начало операции')
    @abstractmethod
    def work_with_task(self):
        pass

class Task(TaskShablon):
    def __init__(self, list: List = [0], operation) -> None:
        super().__init__(list, operation)

    def work_with_task(self):
        return super().work_with_task()


class Results:
    def __init__(self) -> None:
        pass
    




    