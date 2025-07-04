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
