# 建造者模式

## 简介

在 Python 的设计模式中，建造者模式是一种创建型模式，主要用于构建复杂对象的各个部分，将构建过程和表示分离，使得同样的构建过程可以创建不同的表示将一个复杂对象的构建过程抽象出来，使用不同的“建造者”来构造对象的不同部分，从而达到灵活组装和解耦构建过程与产品结构的目的

## 实战场景

在著名的python开源项目 sqlalchemy 中，使用了建造者模式去构建Query查询对象，用来动态拼接 SQL 查询，比如 SELECT ... WHERE ... ORDER BY ... LIMIT ...。

例如：

```python
class SQLQueryBuilder:
    def __init__(self):
        self._select = "*"
        self._table = ""
        self._where = []
        self._order_by = ""
        self._limit = ""

    def select(self, columns):
        self._select = ", ".join(columns)
        return self

    def from_table(self, table):
        self._table = table
        return self

    def where(self, condition):
        self._where.append(condition)
        return self

    def order_by(self, field):
        self._order_by = field
        return self

    def limit(self, count):
        self._limit = f"LIMIT {count}"
        return self

    def build(self):
        query = f"SELECT {self._select} FROM {self._table}"
        if self._where:
            query += " WHERE " + " AND ".join(self._where)
        if self._order_by:
            query += f" ORDER BY {self._order_by}"
        if self._limit:
            query += f" {self._limit}"
        return query + ";"

# 用法
sql = (
    SQLQueryBuilder()
    .select(["id", "name"])
    .from_table("users")
    .where("age > 18")
    .where("status = 'active'")
    .order_by("created_at")
    .limit(10)
    .build()
)
print(sql)
# 输出：
# SELECT id, name FROM users WHERE age > 18 AND status = 'active' ORDER BY created_at LIMIT 10;
```

## 示例

- [建造者模式代码示例](builder.py)
- [建造者模式测试用例](../../../tests/creational/builder/test_builder.py)
