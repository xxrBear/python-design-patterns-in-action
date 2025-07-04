import unittest
from unittest.mock import MagicMock, patch

from examples.structural.proxy.proxy_file import File, FileProxy


class TestFileProxy(unittest.TestCase):
    def test_admin_can_delete_file(self):
        mock_file = MagicMock(spec=File)
        proxy = FileProxy(user="admin", file=mock_file)

        proxy.delete()

        mock_file.delete.assert_called_once()

    def test_guest_cannot_delete_file(self):
        mock_file = MagicMock(spec=File)
        proxy = FileProxy(user="guest", file=mock_file)

        with patch("builtins.print") as mock_print:
            proxy.delete()
            mock_file.delete.assert_not_called()
            mock_print.assert_called_with("Permission denied.")


if __name__ == "__main__":
    unittest.main()
