# 抽象工厂方法模式

## 简介
抽象工厂方法提供一系列相关产品的创建接口，不指定具体类。抽象工厂方法们需要多写点东西

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

这样便能解决简单工厂模式下，增加新子类，需要修改创建方法的缺陷。也可以解决工厂方法下类爆炸问题，接口统一多个产品族，避免过度暴露细节