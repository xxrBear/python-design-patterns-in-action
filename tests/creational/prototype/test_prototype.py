import unittest

from examples.creational.prototype.prototype import (
    Prototype,
    PrototypeRegistry,
)


class TestPrototypePattern(unittest.TestCase):
    def setUp(self):
        self.registry = PrototypeRegistry()
        self.prototype_a = Prototype("ItemA", [1, 2, 3])  # 注意用列表测试浅拷贝
        self.registry.register("item_a", self.prototype_a)

    def test_clone_creates_new_object(self):
        cloned = self.registry.clone("item_a")
        self.assertIsNot(cloned, self.prototype_a)  # 确保不是同一个对象
        self.assertEqual(cloned.name, "ItemA")
        self.assertEqual(cloned.value, [1, 2, 3])

    def test_clone_is_shallow_copy(self):
        cloned = self.registry.clone("item_a")
        cloned.value.append(4)
        # 因为是浅拷贝，原型的值也会变化
        self.assertEqual(self.prototype_a.value, [1, 2, 3, 4])

    def test_clone_nonexistent_key(self):
        with self.assertRaises(ValueError):
            self.registry.clone("nonexistent")
