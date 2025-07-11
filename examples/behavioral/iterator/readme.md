# 迭代器模式 

## 简介
迭代器模式是一种行为型设计模式，用于顺序访问一个集合对象中的元素，而不暴露其内部表示结构。

它的目的是将集合的遍历操作从集合对象中分离出来，实现 统一访问方式。

## 示例
```python
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
```