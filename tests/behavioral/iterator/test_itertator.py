import unittest

from examples.behavioral.iterator.itertator import NumberCollection


class TestNumberIterator(unittest.TestCase):
    def test_iteration(self):
        data = [10, 20, 30]
        collection = NumberCollection(data)
        result = []

        for num in collection:
            result.append(num)

        self.assertEqual(result, data)

    def test_empty_collection(self):
        collection = NumberCollection([])
        result = [x for x in collection]
        self.assertEqual(result, [])

    def test_iterator_manual_next(self):
        data = [1, 2]
        iterator = NumberCollection(data).__iter__()
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)
        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == "__main__":
    unittest.main()
