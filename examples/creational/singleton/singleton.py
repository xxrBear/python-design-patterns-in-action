# ----------------------------------------------------------------------------------------------------
# 单例模式
#
# 作者：xxrBear
# 创建时间：2025-06-19
# ----------------------------------------------------------------------------------------------------


class Singleton:
    """最简单的单例模式"""

    _instance = None

    def __new__(cls):
        if cls is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return cls._instance


if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    print(a is b)
