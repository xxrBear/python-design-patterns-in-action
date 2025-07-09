# 装饰器模式

## 简介
装饰器可能是Python开发者最熟悉的功能之一了，它们不仅在标准库中存在，同时也在三方库中大量使用，如果你写过Python程序，那么你百分百用过Python的装饰器，不过，我们要介绍的装饰器模式虽然与Python装饰器很像，但它两并不是一个东西。装饰器模式和Python装饰器相同的一点是，它们的功能都是在不改动原有被装饰对象的基础上，为被装饰对象添加新的功能和扩展，但是Python装饰器只是一种语法糖，或者可以说，Python装饰器是装饰器模式的一种实现。

## 示例
```python
# 基础类（被装饰对象）
class Coffee:
    def cost(self):
        return 10

# 装饰器类（包装对象）
class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2  # 加糖 +2 元
```