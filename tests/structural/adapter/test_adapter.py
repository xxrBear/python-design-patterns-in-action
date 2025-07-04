import unittest
from unittest.mock import MagicMock

from examples.structural.adapter.adapter import DBAdapter, OldDB


class TestDBAdapter(unittest.TestCase):
    def test_adapter_calls_old_methods(self):
        # 创建 OldDB 的 mock 实例
        mock_old_db = MagicMock(spec=OldDB)

        adapter = DBAdapter(mock_old_db)

        # 测试 connect_db 是否调用了 old_db.connect
        adapter.connect_db()
        mock_old_db.connect.assert_called_once()

        # 测试 execute_query 是否调用了 old_db.run_sql
        sql = "SELECT * FROM users"
        adapter.execute_query(sql)
        mock_old_db.run_sql.assert_called_once_with(sql)


if __name__ == "__main__":
    unittest.main()
