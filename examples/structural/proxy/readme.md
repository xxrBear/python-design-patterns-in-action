# 代理模式

**定义**：代理模式为某个对象提供一个“代理”对象，并由代理对象控制对原对象的访问

> 本质：**控制访问**，可以在访问目标对象前后添加逻辑


## 二、适用场景

代理模式主要用于以下场景：

| 类型                            | 描述                                                     |
| ------------------------------- | -------------------------------------------------------- |
| 远程代理（Remote Proxy）        | 为在不同地址空间的对象提供访问接口（如 RPC、数据库连接） |
| 虚拟代理（Virtual Proxy）       | 延迟加载资源，只有在需要时才创建真实对象（如大图加载）   |
| 保护代理（Protection Proxy）    | 控制权限，比如不同用户是否可以访问目标对象               |
| 智能引用代理（Smart Reference） | 在访问对象时自动执行某些附加操作（如引用计数、日志记录） |


## 示例

### 示例：虚拟代理（懒加载大图）

```python
from time import sleep

# 抽象接口
class Image:
    def display(self):
        raise NotImplementedError

# 实际类：很耗资源
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading image {self.filename}...")
        sleep(2)  # 模拟耗时加载

    def display(self):
        print(f"Displaying {self.filename}")

# 虚拟代理
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if not self._real_image:
            self._real_image = RealImage(self.filename)
        self._real_image.display()

img = ProxyImage("photo.jpg") 
print("Image created")  
img.display()  # 此时才加载图片
img.display()  # 不再加载
```

* Proxy 延迟了真实图片对象的创建
* 提高性能，节省资源


### 示例：保护代理（访问权限控制）

```python
class File:
    def __init__(self, filename):
        self.filename = filename

    def delete(self):
        print(f"{self.filename} deleted.")

# 代理类
class FileProxy:
    def __init__(self, user, file: File):
        self.user = user
        self.file = file

    def delete(self):
        if self.user == "admin":
            self.file.delete()
        else:
            print("Permission denied.")

# 测试
proxy1 = FileProxy("admin", File("data.txt"))
proxy2 = FileProxy("guest", File("data.txt"))

proxy1.delete()
proxy2.delete()
```

## 数据库连接池代理

我们模拟一个数据库连接池代理，避免每次都新建连接

```python
class DBConnection:
    def __init__(self, conn_id):
        self.conn_id = conn_id
        print(f"Create new connection {conn_id}")

    def query(self, sql):
        print(f"[{self.conn_id}] Executing: {sql}")

class ConnectionPoolProxy:
    def __init__(self, size=2):
        self.size = size
        self._pool = []
        self._used = []

    def get_connection(self):
        if self._pool:
            conn = self._pool.pop()
            self._used.append(conn)
            return conn
        elif len(self._used) < self.size:
            conn = DBConnection(len(self._used) + 1)
            self._used.append(conn)
            return conn
        else:
            raise Exception("No available connections.")

    def release(self, conn):
        self._used.remove(conn)
        self._pool.append(conn)

# 使用连接池
proxy = ConnectionPoolProxy(size=2)

conn1 = proxy.get_connection()
conn1.query("SELECT * FROM users")
proxy.release(conn1)

conn2 = proxy.get_connection()
conn2.query("SELECT * FROM orders")
```
