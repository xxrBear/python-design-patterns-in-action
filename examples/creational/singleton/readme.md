# 单例模式

## 简介
单例模式（Singleton Pattern） 是最常见、最简单的设计模式之一，其核心思想是：保证一个类在系统中只能有一个实例，并提供全局访问点。这在需要统一管理某些全局资源或状态时非常有用。

## 经典的应用场景

### 配置管理器

应用程序运行时往往需要读取配置参数（例如 Django 的 settings 对象）确保系统中始终只有一份配置对象，避免重复加载、重复解析，浪费系统资源。

### 日志记录器

在大型系统中，统一的日志管理尤为重要。使用单例可以保证所有模块共享同一个日志实例，方便日志集中写入与管理。

## 最简单的单例模式

```python
class Singleton:
    """最简单的单例模式"""

    _instance = None

    def __new__(cls):
        if cls is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return cls._instance
```

这是最简单的单例模式，如果你创建这个类的实例，你会发现无论创建多少次，实例对象都是同一个。

## 多线程版本的单例模式

```python
class MultiThreadSingleton:
    """多线程版本"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                cls._instance = super().__new__(cls)
                return cls._instance
        else:
            return cls._instance
```

在最简单的单例模式示例中，还是可能重复创建实例的，例如多线程创建对象，当一个线程进入`__new__`方法时，在没有创建实例时，另一个线程也进入此方法，这时就可能重复创建实例，解决方法是加入线程锁，当一个线程进入方法时，它会拿到锁，此时其余的线程因为锁的原因，阻塞，无进入此方法，创建结束锁释放，此时直接返回单例对象。

## 利用Python特性实现单例模式

在上面的方法中，我们都是通过写一个类来实现一个单例，但其实我们可以利用python的模块导入的特性来生成单例。

python的模块导入有且只会有一次，如果你不显示的使用`reload`方法调用的话，无论`import`多少次，模块只会加载一次，利用这个特性，我们只需要在模块中实例话这个类，然后在使用它的地方导入这个类实例即可实现单例模式。

```python
class S:
    pass

s = S()

# 使用时
from xxx import s
```

在 Python 项目中，若没有特殊需求（如懒加载或多进程安全），优先使用模块级单例来简化设计，既符合 Python 语言风格，又降低了维护成本。
