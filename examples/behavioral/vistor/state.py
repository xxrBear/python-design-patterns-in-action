from abc import ABC, abstractmethod


# 元素接口
class Employee(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# 具体元素：工程师
class Engineer(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_engineer(self)


# 具体元素：经理
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def accept(self, visitor):
        visitor.visit_manager(self)
