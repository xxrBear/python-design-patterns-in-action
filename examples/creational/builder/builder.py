from abc import ABC, abstractmethod


class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.disk = None

    def __str__(self):
        return f"CPU: {self.cpu}, Memory: {self.memory}, Disk: {self.disk}"


class Builder(ABC):
    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_memory(self):
        pass

    @abstractmethod
    def build_disk(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def with_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def with_memory(self, memory):
        self.computer.memory = memory
        return self

    def with_disk(self, disk):
        self.computer.disk = disk
        return self

    def build(self):
        return self.computer
