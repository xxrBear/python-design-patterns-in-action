# 原型模式

## 简介

原型模式的核心思想是：**通过复制现有对象（原型）来创建新对象，而不是通过实例化类来创建。**

这尤其适用于创建成本高或复杂对象结构的场景


## 使用场景

原型模式适用于以下情况：

* 创建对象的成本较高（如数据库连接、大对象初始化等）
* 需要多个相似对象，且它们之间只有少量不同


## 实现原型模式

Python 中可使用内置的 `copy` 模块中的 `copy()`（浅拷贝）或 `deepcopy()`（深拷贝）方法来实现原型复制

### 基本结构

1. **原型接口**：定义 clone 方法（Python中可用标准接口或自定义）
2. **具体原型类**：实现 clone 方法
3. **使用者**：通过调用原型的 clone 方法来创建新对象

## 示例

```python

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
```

## 浅拷贝 vs 深拷贝

| 类型                    | 描述                                                     |
| ----------------------- | -------------------------------------------------------- |
| 浅拷贝（copy.copy）     | 对于不可变数据类型是新创建，对于可变数据类型是引用原对象 |
| 深拷贝（copy.deepcopy） | 对于任何数据类型都是新创建对象                           |


## 优点

* **提高对象创建效率**：避免重复构造
* **运行时灵活复制**：可动态复制现有对象，避免过度依赖构造器
* **降低耦合**：调用者不需要知道如何创建复杂对象


## 注意事项

* 要保证被复制的对象及其内部引用对象都能正确复制（实现 `__deepcopy__`）
* 对于大型对象结构，深拷贝可能会有性能开销
* 原型模式不适用于所有场景，尤其是对象结构较简单时会引入不必要的复杂性
