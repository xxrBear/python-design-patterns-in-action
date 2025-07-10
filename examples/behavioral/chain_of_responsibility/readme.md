# 责任链模式 

## 简介
责任链模式是一种行为型设计模式，允许多个对象都有机会处理请求，将这些对象连接成一条链，请求沿着链传递，直到被某个对象处理为止。


## 示例
```python
from abc import ABC, abstractmethod

# 抽象处理者
class Handler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, next_handler):
        self._next = next_handler
        return next_handler  # 支持链式调用

    @abstractmethod
    def handle(self, days):
        pass

# 具体处理者
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

# 使用
team_leader = TeamLeader()
manager = Manager()
director = Director()

team_leader.set_next(manager).set_next(director)

team_leader.handle(1)
team_leader.handle(2)
team_leader.handle(5)
team_leader.handle(10)
```