import sys
import unittest
from io import StringIO

from examples.structural.bridge.bridge import (
    EmailSender,
    Message,
    SMSSender,
    UrgentMessage,
)


class TestBridgePattern(unittest.TestCase):
    def setUp(self):
        # 重定向 stdout，用于捕获 print 输出
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # 还原 stdout
        sys.stdout = sys.__stdout__

    def test_email_message(self):
        sender = EmailSender()
        msg = Message(sender)
        msg.send("测试邮件")
        output = self.held_stdout.getvalue().strip()
        self.assertEqual(output, "用邮件发送消息: 测试邮件")

    def test_sms_urgent_message(self):
        sender = SMSSender()
        urgent_msg = UrgentMessage(sender)
        urgent_msg.send("测试短信")
        output = self.held_stdout.getvalue().strip()
        self.assertEqual(output, "用短信发送消息: [紧急] 测试短信")


if __name__ == "__main__":
    unittest.main()
