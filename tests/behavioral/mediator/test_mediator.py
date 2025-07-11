import unittest
from unittest.mock import MagicMock

from examples.behavioral.mediator.mediator import ChatRoomMediator, User


class TestChatRoomMediator(unittest.TestCase):
    def test_register_and_send(self):
        mediator = ChatRoomMediator()

        # 创建用户并注入 mock 的 receive 方法
        user1 = User("Alice", mediator)
        user2 = User("Bob", mediator)
        user3 = User("Charlie", mediator)

        # 替换 receive 方法为 mock，便于捕获调用
        user1.receive = MagicMock()
        user2.receive = MagicMock()
        user3.receive = MagicMock()

        # 注册用户
        mediator.register(user1)
        mediator.register(user2)
        mediator.register(user3)

        # Alice 发送消息
        user1.send("Hello everyone")

        # 验证 Bob 和 Charlie 收到了消息（但 Alice 自己不会）
        user2.receive.assert_called_once_with("Hello everyone")
        user3.receive.assert_called_once_with("Hello everyone")
        user1.receive.assert_not_called()


if __name__ == "__main__":
    unittest.main()
