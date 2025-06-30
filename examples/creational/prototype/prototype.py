class Prototype:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def clone(self):
        return Prototype(self.name, self.value)  # 浅拷贝

    def __str__(self):
        return f"{self.name}: {self.value}"


class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, key, prototype):
        self._prototypes[key] = prototype

    def clone(self, key):
        prototype = self._prototypes.get(key)
        if not prototype:
            raise ValueError(f"No prototype registered under '{key}'")
        return prototype.clone()
