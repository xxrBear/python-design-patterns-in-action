import sys
import unittest
from io import StringIO

from examples.structural.flyweight.flyweight import FlyweightFactory


class TestFlyweightPattern(unittest.TestCase):
    def setUp(self):
        # 重定向 stdout 以捕获 print 输出
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

        self.factory = FlyweightFactory()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_flyweight_sharing(self):
        fw1 = self.factory.get_flyweight("黑色棋子")
        fw2 = self.factory.get_flyweight("黑色棋子")
        fw3 = self.factory.get_flyweight("白色棋子")

        self.assertIs(fw1, fw2)  # 应该是同一个实例
        self.assertIsNot(fw1, fw3)  # 不同实例

    def test_flyweight_operation_output(self):
        fw = self.factory.get_flyweight("黑色棋子")
        fw.operation("位置A1")
        output = self.captured_output.getvalue().strip()
        expected = "内部状态: 黑色棋子, 外部状态: 位置A1"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
