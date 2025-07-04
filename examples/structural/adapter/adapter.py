class OldDB:
    def connect(self):
        print("连接老数据库...")

    def run_sql(self, sql):
        print(f"执行 SQL：{sql}")


class NewDBInterface:
    def connect_db(self):
        raise NotImplementedError

    def execute_query(self, sql):
        raise NotImplementedError


class DBAdapter(NewDBInterface):
    def __init__(self, old_db):
        self.old_db = old_db

    def connect_db(self):
        self.old_db.connect()

    def execute_query(self, sql):
        self.old_db.run_sql(sql)
