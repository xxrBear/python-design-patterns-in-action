import sys
import unittest
from io import StringIO

from examples.structural.facade.facade import (
    DVDPlayer,
    HomeTheaterFacade,
    Projector,
    TheaterLights,
)

# 假设你的类都在当前作用域，或者从模块导入：
# from your_module import DVDPlayer, Projector, TheaterLights, HomeTheaterFacade


class TestHomeTheaterFacade(unittest.TestCase):
    def setUp(self):
        # 捕获标准输出
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

        # 初始化子系统和外观
        self.dvd = DVDPlayer()
        self.projector = Projector()
        self.lights = TheaterLights()
        self.home_theater = HomeTheaterFacade(self.dvd, self.projector, self.lights)

    def tearDown(self):
        # 恢复标准输出
        sys.stdout = sys.__stdout__

    def test_watch_movie(self):
        self.home_theater.watch_movie()
        output = self.captured_output.getvalue()
        expected = (
            "准备观看电影...\n"
            "灯光调暗\n"
            "投影仪开启\n"
            "投影仪设置为宽屏模式\n"
            "DVD播放器开启\n"
            "DVD开始播放\n"
        )
        self.assertEqual(output, expected)

    def test_end_movie(self):
        self.home_theater.end_movie()
        output = self.captured_output.getvalue()
        expected = "结束观看电影...\nDVD播放器关闭\n投影仪关闭\n灯光开启\n"
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
