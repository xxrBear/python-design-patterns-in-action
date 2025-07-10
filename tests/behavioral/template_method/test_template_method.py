import sys
import unittest
from io import StringIO

from examples.behavioral.template_method.template_method import (
    ConcreteClassA,
    ConcreteClassB,
)


class TestTemplateMethod(unittest.TestCase):
    def setUp(self):
        # 捕获标准输出
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        # 还原标准输出
        sys.stdout = self.original_stdout

    def test_concrete_class_a(self):
        obj = ConcreteClassA()
        obj.template_method()
        output = self.held_output.getvalue()
        self.assertIn("Step 1: 通用处理", output)
        self.assertIn("Step 2A: 子类实现的步骤", output)
        self.assertIn("Step 3: 可选通用步骤", output)

    def test_concrete_class_b(self):
        obj = ConcreteClassB()
        obj.template_method()
        output = self.held_output.getvalue()
        self.assertIn("Step 1: 通用处理", output)
        self.assertIn("Step 2B: 子类实现的不同步骤", output)
        self.assertIn("Step 3: 可选通用步骤", output)


if __name__ == "__main__":
    unittest.main()
