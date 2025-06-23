# ----------------------------------------------------------------------------------------------------
# 单例模式
#
# 作者：xxrBear
# 创建时间：2025-06-19
# ----------------------------------------------------------------------------------------------------


import threading


class Singleton:
    """最简单的单例模式"""

    _instance = None

    def __new__(cls):
        if cls is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return cls._instance


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
