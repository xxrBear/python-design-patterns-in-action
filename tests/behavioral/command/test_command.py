import sys
import unittest
from io import StringIO

from examples.behavioral.command.command import (
    Light,
    LightOffCommand,
    LightOnCommand,
    RemoteControl,
)


class TestCommandPattern(unittest.TestCase):
    def setUp(self):
        self.light = Light()
        self.light_on_command = LightOnCommand(self.light)
        self.light_off_command = LightOffCommand(self.light)
        self.remote = RemoteControl()

        # 捕获输出
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_light_on_command(self):
        self.remote.set_command(self.light_on_command)
        self.remote.press_button()
        self.assertIn("灯打开了", self.output.getvalue())

    def test_light_off_command(self):
        self.remote.set_command(self.light_off_command)
        self.remote.press_button()
        self.assertIn("灯关闭了", self.output.getvalue())


if __name__ == "__main__":
    unittest.main()
