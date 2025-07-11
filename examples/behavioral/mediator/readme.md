# 中介者模式

## 简介
中介者模式是一种行为型设计模式，它通过引入一个中介对象来封装一组对象之间的交互，使得这些对象不再互相引用，而是通过中介者来进行通信，从而降低对象之间的耦合度。


## 示例
```python
from abc import ABC, abstractmethod

# 抽象中介者
class Mediator(ABC):
    @abstractmethod
    def send(self, message: str, colleague):
        pass

# 抽象同事类
class Colleague(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

    @abstractmethod
    def receive(self, message: str):
        pass

# 具体同事类
class User(Colleague):
    def __init__(self, name: str, mediator):
        super().__init__(mediator)
        self.name = name

    def send(self, message: str):
        print(f"{self.name} 发送消息：{message}")
        self.mediator.send(message, self)

    def receive(self, message: str):
        print(f"{self.name} 收到消息：{message}")

class ChatRoomMediator(Mediator):
    def __init__(self):
        self.users = []

    def register(self, user: User):
        self.users.append(user)

    def send(self, message: str, sender: User):
        for user in self.users:
            if user != sender:
                user.receive(message)

```