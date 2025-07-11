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
