# 工厂方法模式

## 简介
工厂方法模式的官方解释是，定义一个用于创建对象的接口，让子类决定实例化哪一个类。工厂方法使一个类的实例化延迟到其子类。

## 简单工厂模式

### 简介
简单工厂模式不是它不是 GoF 23 个正式设计模式之一，但在实际开发中非常常用，尤其是小型场景。

### 使用场景
需要根据不同条件，创建不同的对象

### 示例

- 简单工厂示例

```python
from abc import ABC, abstractmethod

# 抽象类
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 具体实现类
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 工厂类
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
```

### 使用方法
```python
if __name__ == "__main__":
    animal1 = AnimalFactory.create_animal("dog")
    print(animal1.speak())  # 输出：Woof!

    animal2 = AnimalFactory.create_animal("cat")
    print(animal2.speak())  # 输出：Meow!
```

### 优缺点
简单工厂方法很简单，利用工厂类来实现子类的创建，它很适合一些小型的代码块任务，但是它也有缺点，它的实现违反了开放-封闭原则（即对修改关闭，对扩展开放），想一想，如果我么嗯要增加一个动物类，我们需要修改`create_animal`方法，这不是很优雅。

## 抽象工厂方法

### 简介
抽象工厂方法可以解决上面简单工厂的缺点，但是我们需要多写点东西

### 示例
```python
# 抽象类
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# 实现类
class WeChatPay(Payment):
    def pay(self, amount: float):
        print(f"微信支付成功，金额：{amount}元")

class AliPay(Payment):
    def pay(self, amount: float):
        print(f"支付宝支付成功，金额：{amount}元")

class BankPay(Payment):
    def pay(self, amount: float):
        print(f"银行卡支付成功，金额：{amount}元")

# 抽象工厂类
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        pass

# 具体工厂类
class WeChatPayFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return WeChatPay()

class AliPayFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return AliPay()

class BankPayFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return BankPay()
```

### 使用注册类
```python
class PaymentFactoryRegistry:
    _factories = {}

    @classmethod
    def register_factory(cls, name: str, factory_cls):
        cls._factories[name] = factory_cls

    @classmethod
    def get_factory(cls, name: str) -> PaymentFactory:
        factory_cls = cls._factories.get(name)
        if not factory_cls:
            raise ValueError(f"No factory registered for {name}")
        return factory_cls()

# 注册
PaymentFactoryRegistry.register_factory('ali', AliPayFactory)
PaymentFactoryRegistry.register_factory('wechat', WeChatPayFactory)

# 业务代码动态获取工厂
factory = PaymentFactoryRegistry.get_factory('ali')
payment = factory.create_payment()
payment.pay(100)
```

这样便能解决简单工厂模式下，增加新子类，需要修改工厂方法的缺陷。
