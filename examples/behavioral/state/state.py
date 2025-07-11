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
