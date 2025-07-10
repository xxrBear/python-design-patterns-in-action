# 模板方法模式

## 简介
模板方法模式（Template Method Pattern） 是一种行为型设计模式，它在一个方法中定义一个算法的骨架，而将一些步骤的实现延迟到子类。这样可以让子类在不改变算法结构的情况下重新定义算法的某些步骤

## 示例
```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        print("Step 1: 通用处理")

    @abstractmethod
    def step2(self):
        pass

    def step3(self):
        print("Step 3: 可选通用步骤")

class ConcreteClassA(AbstractClass):
    def step2(self):
        print("Step 2A: 子类实现的步骤")

class ConcreteClassB(AbstractClass):
    def step2(self):
        print("Step 2B: 子类实现的不同步骤")

# 使用
obj = ConcreteClassA()
obj.template_method()
```