# 命令模式 

## 简介
命令模式是一种行为型设计模式，它的核心思想是将“请求”封装成一个命令对象，从而使你可以用不同的请求、队列请求或者日志请求，以及支持可撤销操作。
换句话说，命令模式将请求发送者与请求执行者解耦，让请求以对象的形式进行传递和处理。

## 示例
```python
from abc import ABC, abstractmethod

# 命令接口
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# 接收者
class Light:
    def turn_on(self):
        print("灯打开了")

    def turn_off(self):
        print("灯关闭了")

# 具体命令：开灯命令
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# 具体命令：关灯命令
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# 调用者
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
```