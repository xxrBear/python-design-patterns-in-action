import sys
import unittest
from abc import ABC, abstractmethod
from io import StringIO


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


class TestTemplateMethodPattern(unittest.TestCase):
    def setUp(self):
        # 捕获标准输出
        self._stdout = sys.stdout
        sys.stdout = self.captured_output = StringIO()

    def tearDown(self):
        # 恢复标准输出
        sys.stdout = self._stdout

    def test_concrete_class_a(self):
        obj = ConcreteClassA()
        obj.template_method()
        output = self.captured_output.getvalue()
        self.assertIn("Step 1: 通用处理", output)
        self.assertIn("Step 2A: 子类实现的步骤", output)
        self.assertIn("Step 3: 可选通用步骤", output)

    def test_concrete_class_b(self):
        obj = ConcreteClassB()
        obj.template_method()
        output = self.captured_output.getvalue()
        self.assertIn("Step 1: 通用处理", output)
        self.assertIn("Step 2B: 子类实现的不同步骤", output)
        self.assertIn("Step 3: 可选通用步骤", output)


if __name__ == "__main__":
    unittest.main()
