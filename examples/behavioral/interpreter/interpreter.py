from abc import ABC, abstractmethod


# 抽象表达式
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass


# 终结符表达式（数字）
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value


# 非终结符表达式（加法）
class Add(Expression):
    def __init__(self, left, right):
        self.left = left  # 左表达式
        self.right = right  # 右表达式

    def interpret(self):
        return self.left.interpret() + self.right.interpret()
