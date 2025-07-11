# 状态模式 

## 简介
状态模式是一种行为型设计模式，允许对象在内部状态发生改变时改变它的行为，就好像它变成了另一个类一样。


## 示例
```python
from abc import ABC, abstractmethod

# 抽象状态类
class State(ABC):
    @abstractmethod
    def toggle(self, context):
        pass

# 具体状态类：关
class OffState(State):
    def toggle(self, context):
        print("当前是[关] → 切换到[开]")
        context.set_state(OnState())

# 具体状态类：开
class OnState(State):
    def toggle(self, context):
        print("当前是[开] → 切换到[关]")
        context.set_state(OffState())

# 上下文：灯
class Light:
    def __init__(self):
        self._state = OffState()  # 初始状态是关

    def set_state(self, state):
        self._state = state

    def press_button(self):
        self._state.toggle(self)
```