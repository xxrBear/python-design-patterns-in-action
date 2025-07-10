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
