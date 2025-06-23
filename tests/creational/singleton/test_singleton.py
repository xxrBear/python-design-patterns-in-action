import threading
import unittest

from examples.creational.singleton.singleton import MultiThreadSingleton, Singleton


class TestSingleton(unittest.TestCase):
    def test_create_sington(self):
        s1 = Singleton()
        s2 = Singleton()
        (self.assertIs(s1, s2), f"{s1} 与 {s2} 不是同一个实例")


class TestMultiThreadSingleton(unittest.TestCase):
    def test_create_thread_safe_sington(self):
        _instance_list = []

        def create_instance():
            i = MultiThreadSingleton()
            _instance_list.append(i)

        threads = []
        for _ in range(10):
            t = threading.Thread(
                target=create_instance,
            )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        ids = {id(obj) for obj in _instance_list}
        self.assertEqual(len(ids), 1)


if __name__ == "__main__":
    unittest.main()
