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
