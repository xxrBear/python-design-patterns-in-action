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
