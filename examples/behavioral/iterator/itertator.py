from collections.abc import Iterator, Iterable


# 自定义聚合类
class NumberCollection(Iterable):
    def __init__(self, numbers):
        self._numbers = numbers

    def __iter__(self):
        return NumberIterator(self._numbers)


# 自定义迭代器
class NumberIterator(Iterator):
    def __init__(self, numbers):
        self._numbers = numbers
        self._index = 0

    def __next__(self):
        if self._index < len(self._numbers):
            result = self._numbers[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
