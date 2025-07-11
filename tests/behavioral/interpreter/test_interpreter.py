import unittest

from examples.behavioral.interpreter.interpreter import Add, Number


class TestInterpreterPattern(unittest.TestCase):
    def test_single_number(self):
        five = Number(5)
        self.assertEqual(five.interpret(), 5)

    def test_simple_add(self):
        expr = Add(Number(3), Number(4))  # 3 + 4
        self.assertEqual(expr.interpret(), 7)

    def test_nested_add(self):
        # (1 + 2) + (3 + 4) = 10
        left = Add(Number(1), Number(2))
        right = Add(Number(3), Number(4))
        expr = Add(left, right)
        self.assertEqual(expr.interpret(), 10)

    def test_negative_number(self):
        expr = Add(Number(-2), Number(5))  # -2 + 5
        self.assertEqual(expr.interpret(), 3)


if __name__ == "__main__":
    unittest.main()
