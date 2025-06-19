import unittest

from examples.creational.singleton.singleton import Singleton


class TestSingleton(unittest.TestCase):
    def test_create_sington(self):
        s1 = Singleton()
        s2 = Singleton()
        (self.assertIs(s1, s2), f"{s1} 与 {s2} 不是同一个实例")


if __name__ == "__main__":
    unittest.main()
