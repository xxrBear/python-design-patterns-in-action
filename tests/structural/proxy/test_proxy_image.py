import unittest
from unittest.mock import MagicMock, patch

from examples.structural.proxy.proxy_img import ProxyImage


class TestProxyImage(unittest.TestCase):
    @patch("examples.structural.proxy.proxy_img.RealImage")  # 替换 RealImage 为 mock
    def test_proxy_image_lazy_loading(self, MockRealImage):
        # 创建一个 mock 实例替代 RealImage
        mock_instance = MagicMock()
        MockRealImage.return_value = mock_instance

        # 初始化 ProxyImage，不应调用 RealImage
        proxy = ProxyImage("test.jpg")
        self.assertIsNone(proxy._real_image)

        # 调用 display：应该初始化 RealImage 并调用其 display
        proxy.display()
        MockRealImage.assert_called_once_with("test.jpg")
        mock_instance.display.assert_called_once()

        # 再次调用 display：不应再次初始化 RealImage
        proxy.display()
        MockRealImage.assert_called_once()  # 确认只初始化一次
        self.assertEqual(mock_instance.display.call_count, 2)  # 调用两次 display


if __name__ == "__main__":
    unittest.main()
