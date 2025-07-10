# 策略模式 

## 简介
策略模式（Strategy Pattern） 是一种行为型设计模式，它将一组可互换的算法封装成独立的类，使得算法可以独立于使用它的客户端变化。这样可以在运行时动态选择使用哪种算法

## 示例
```python
from abc import ABC, abstractmethod

# 抽象策略
class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

# 具体策略A：升序排序
class AscendingStrategy(Strategy):
    def execute(self, data):
        return sorted(data)

# 具体策略B：降序排序
class DescendingStrategy(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

# 上下文类
class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        return self.strategy.execute(data)

# 使用示例
data = [5, 2, 9, 1]

context = Context(AscendingStrategy())
print("升序：", context.execute_strategy(data))

context.set_strategy(DescendingStrategy())
print("降序：", context.execute_strategy(data))
```