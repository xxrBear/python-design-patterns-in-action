from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, next_handler):
        self._next = next_handler
        return next_handler

    @abstractmethod
    def handle(self, days):
        pass


class TeamLeader(Handler):
    def handle(self, days):
        if days <= 1:
            print("TeamLeader: 批准 1 天请假")
        elif self._next:
            self._next.handle(days)
        else:
            print("请假天数过长，无法批准")


class Manager(Handler):
    def handle(self, days):
        if days <= 3:
            print("Manager: 批准 3 天以内请假")
        elif self._next:
            self._next.handle(days)
        else:
            print("请假天数过长，无法批准")


class Director(Handler):
    def handle(self, days):
        if days <= 7:
            print("Director: 批准 7 天以内请假")
        else:
            print("Director: 拒绝，请假太长")
