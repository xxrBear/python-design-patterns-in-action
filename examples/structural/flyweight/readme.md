# 享元模式 

## 简介
享元模式（Flyweight Pattern）是一种结构型设计模式，主要目的是通过共享大量细粒度对象，减少内存使用，提高效率。

## 示例
```python
class Flyweight:
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state  # 内部状态

    def operation(self, extrinsic_state):
        print(f"内部状态: {self.intrinsic_state}, 外部状态: {extrinsic_state}")

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = Flyweight(key)
        return self._flyweights[key]

if __name__ == "__main__":
    factory = FlyweightFactory()
    fw1 = factory.get_flyweight("黑色棋子")
    fw2 = factory.get_flyweight("黑色棋子")
    fw3 = factory.get_flyweight("白色棋子")

    print(fw1 is fw2)  # True，共享同一个对象
    fw1.operation("位置A1")
    fw3.operation("位置B2")

```