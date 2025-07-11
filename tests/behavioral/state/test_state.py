import unittest
from io import StringIO
from unittest.mock import patch

from examples.behavioral.state.state import Light


class TestStatePattern(unittest.TestCase):
    def test_toggle_states(self):
        light = Light()

        with patch("sys.stdout", new=StringIO()) as fake_out:
            light.press_button()  # 初始为 Off → 切换到 On
            output1 = fake_out.getvalue().strip()
            self.assertIn("当前是[关] → 切换到[开]", output1)

        with patch("sys.stdout", new=StringIO()) as fake_out:
            light.press_button()  # On → Off
            output2 = fake_out.getvalue().strip()
            self.assertIn("当前是[开] → 切换到[关]", output2)

        with patch("sys.stdout", new=StringIO()) as fake_out:
            light.press_button()  # Off → On again
            output3 = fake_out.getvalue().strip()
            self.assertIn("当前是[关] → 切换到[开]", output3)


if __name__ == "__main__":
    unittest.main()
