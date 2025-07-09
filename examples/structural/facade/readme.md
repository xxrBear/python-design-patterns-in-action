# 外观模式 

## 简介
外观模式为复杂的子系统提供一个简单的接口，客户端只需要与这个接口交互，而不用关心子系统的内部细节。



## 示例
```python
# 子系统
class DVDPlayer:
    def on(self):
        print("DVD播放器开启")

    def play(self):
        print("DVD开始播放")

    def off(self):
        print("DVD播放器关闭")

class Projector:
    def on(self):
        print("投影仪开启")

    def wide_screen_mode(self):
        print("投影仪设置为宽屏模式")

    def off(self):
        print("投影仪关闭")

class TheaterLights:
    def dim(self):
        print("灯光调暗")

    def on(self):
        print("灯光开启")

# 外观
class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, projector: Projector, lights: TheaterLights):
        self.dvd = dvd
        self.projector = projector
        self.lights = lights

    def watch_movie(self):
        print("准备观看电影...")
        self.lights.dim()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.dvd.on()
        self.dvd.play()

    def end_movie(self):
        print("结束观看电影...")
        self.dvd.off()
        self.projector.off()
        self.lights.on()

# 客户端
if __name__ == "__main__":
    dvd = DVDPlayer()
    projector = Projector()
    lights = TheaterLights()

    home_theater = HomeTheaterFacade(dvd, projector, lights)
    home_theater.watch_movie()
    print("---电影播放中---")
    home_theater.end_movie()
```