# 命令模式 

## 简介
解释器模式是一种行为型设计模式，用于给定一种语言，定义它的文法表示，并设计一个解释器来解释语言中的句子。

简单来说，解释器模式通过构建抽象语法树（AST），将复杂的语法规则封装成一组类，每个类负责解释文法中的一个规则，实现对语言的解析和执行。

## 示例
```python
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
```