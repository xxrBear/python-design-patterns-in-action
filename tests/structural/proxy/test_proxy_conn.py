import unittest
from unittest.mock import MagicMock, patch

from examples.structural.proxy.proxy_conn import ConnectionPoolProxy, DBConnection


class TestConnectionPoolProxy(unittest.TestCase):
    @patch("examples.structural.proxy.proxy_conn.DBConnection")
    def test_get_connection_under_limit(self, MockDBConnection):
        conn1 = MagicMock()
        conn2 = MagicMock()
        MockDBConnection.side_effect = [conn1, conn2]

        pool = ConnectionPoolProxy(size=2)
        c1 = pool.get_connection()
        c2 = pool.get_connection()

        self.assertEqual(c1, conn1)
        self.assertEqual(c2, conn2)
        self.assertEqual(len(pool._used), 2)

    @patch("examples.structural.proxy.proxy_conn.DBConnection")
    def test_get_connection_exceed_limit(self, MockDBConnection):
        pool = ConnectionPoolProxy(size=1)
        pool.get_connection()  # 占用一个
        with self.assertRaises(Exception) as ctx:
            pool.get_connection()
        self.assertIn("No available connections", str(ctx.exception))

    @patch("examples.structural.proxy.proxy_conn.DBConnection")
    def test_reuse_connection_after_release(self, MockDBConnection):
        conn1 = MagicMock()
        MockDBConnection.return_value = conn1

        pool = ConnectionPoolProxy(size=1)
        c1 = pool.get_connection()
        pool.release(c1)

        c2 = pool.get_connection()
        self.assertEqual(c1, c2)
        self.assertEqual(len(pool._used), 1)
        self.assertEqual(len(pool._pool), 0)


if __name__ == "__main__":
    unittest.main()
