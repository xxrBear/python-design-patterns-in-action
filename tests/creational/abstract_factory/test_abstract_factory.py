import unittest

from examples.creational.abstract_factory.abstract_factory import (
    AliPay,
    AliPayFactory,
    BankPay,
    BankPayFactory,
    PaymentFactoryRegistry,
    WeChatPay,
    WeChatPayFactory,
)


class TestPaymentFactoryRegistry(unittest.TestCase):
    def test_registered_factories(self):
        """测试工厂是否成功注册并返回正确实例"""

        # 测试微信工厂
        factory = PaymentFactoryRegistry.get_factory("wechat")
        self.assertIsInstance(factory, WeChatPayFactory)
        payment = factory.create_payment()
        self.assertIsInstance(payment, WeChatPay)
        self.assertEqual(payment.pay(100), "微信支付成功，金额：100元")

        # 测试支付宝工厂
        factory = PaymentFactoryRegistry.get_factory("ali")
        self.assertIsInstance(factory, AliPayFactory)
        payment = factory.create_payment()
        self.assertIsInstance(payment, AliPay)
        self.assertEqual(payment.pay(200), "支付宝支付成功，金额：200元")

        # 测试银行卡工厂
        factory = PaymentFactoryRegistry.get_factory("bank")
        self.assertIsInstance(factory, BankPayFactory)
        payment = factory.create_payment()
        self.assertIsInstance(payment, BankPay)
        self.assertEqual(payment.pay(300), "银行卡支付成功，金额：300元")

    def test_unregistered_factory(self):
        """测试获取未注册工厂时抛出异常"""
        with self.assertRaises(ValueError):
            PaymentFactoryRegistry.get_factory("unknown")


if __name__ == "__main__":
    unittest.main()
