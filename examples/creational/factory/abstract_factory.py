from abc import ABC, abstractmethod


# 抽象支付接口
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


# 实现类
class WeChatPay(Payment):
    def pay(self, amount: float):
        return f"微信支付成功，金额：{amount}元"


class AliPay(Payment):
    def pay(self, amount: float):
        return f"支付宝支付成功，金额：{amount}元"


class BankPay(Payment):
    def pay(self, amount: float):
        return f"银行卡支付成功，金额：{amount}元"


# 抽象工厂
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        pass


# 具体工厂
class WeChatPayFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return WeChatPay()


class AliPayFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return AliPay()


class BankPayFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return BankPay()


# 工厂注册表
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


# 注册工厂
PaymentFactoryRegistry.register_factory("ali", AliPayFactory)
PaymentFactoryRegistry.register_factory("wechat", WeChatPayFactory)
PaymentFactoryRegistry.register_factory("bank", BankPayFactory)
