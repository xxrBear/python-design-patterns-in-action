# 适配器模式

适配器模式（Adapter Pattern） 是一种结构型设计模式，它的作用是：

将一个类的接口转换成客户端期望的另一个接口，使原本接口不兼容的类能够一起工作

## 简单的示例

场景：你有一个老的数据库连接类 `OldDB`，它使用 `connect()` 和 `run_sql()` 方法

但你现在想统一使用新接口：`connect_db()` 和 `execute_query()`

你不想改旧代码，就可以写个**适配器**


```python
class OldDB:
    def connect(self):
        print("连接老数据库...")

    def run_sql(self, sql):
        print(f"执行 SQL：{sql}")
```


```python
class NewDBInterface:
    def connect_db(self):
        raise NotImplementedError

    def execute_query(self, sql):
        raise NotImplementedError
```

适配器（将旧方法适配为新接口）

```python
class DBAdapter(NewDBInterface):
    def __init__(self, old_db):
        self.old_db = old_db

    def connect_db(self):
        self.old_db.connect()

    def execute_query(self, sql):
        self.old_db.run_sql(sql)
```
