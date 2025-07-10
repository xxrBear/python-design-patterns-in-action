import sys
import unittest
from io import StringIO

from examples.behavioral.observers.observers import (
    AirConditioner,
    PhoneDisplay,
    WeatherStation,
)


class TestObserverPattern(unittest.TestCase):
    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = self._captured_output = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    def test_observer_notification(self):
        weather = WeatherStation()
        phone = PhoneDisplay()
        ac = AirConditioner()

        weather.attach(phone)
        weather.attach(ac)

        weather.set_temperature(28)
        output = self._captured_output.getvalue()

        # 验证温度设置和所有观察者响应
        self.assertIn("[WeatherStation] 温度更新为：28°C", output)
        self.assertIn("[PhoneDisplay] 显示温度：28°C", output)
        self.assertIn("[AirConditioner] 启动制冷", output)

        self._captured_output.truncate(0)
        self._captured_output.seek(0)

        weather.set_temperature(22)
        output = self._captured_output.getvalue()
        self.assertIn("[PhoneDisplay] 显示温度：22°C", output)
        self.assertIn("[AirConditioner] 关闭空调", output)

    def test_observer_detach(self):
        weather = WeatherStation()
        phone = PhoneDisplay()
        ac = AirConditioner()

        weather.attach(phone)
        weather.attach(ac)
        weather.detach(ac)

        weather.set_temperature(30)
        output = self._captured_output.getvalue()

        self.assertIn("[PhoneDisplay] 显示温度：30°C", output)
        self.assertNotIn("[AirConditioner]", output)  # 没有AC响应


if __name__ == "__main__":
    unittest.main()
