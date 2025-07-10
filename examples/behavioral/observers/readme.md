# 观察者模式

## 简介
观察者模式定义了一种一对多的依赖关系，当被观察对象（Subject）的状态发生变化时，会自动通知所有依赖它的观察者对象（Observers），从而实现解耦。


## 示例
```python
from abc import ABC, abstractmethod

# 抽象观察者
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# 被观察者（天气站）
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, value):
        self._temperature = value
        print(f"[WeatherStation] 温度更新为：{value}°C")
        self.notify()

# 具体观察者
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"[PhoneDisplay] 显示温度：{temperature}°C")

class AirConditioner(Observer):
    def update(self, temperature):
        if temperature > 26:
            print("[AirConditioner] 启动制冷")
        else:
            print("[AirConditioner] 关闭空调")

# 使用
weather = WeatherStation()
phone = PhoneDisplay()
ac = AirConditioner()

weather.attach(phone)
weather.attach(ac)

weather.set_temperature(28)
weather.set_temperature(22)
```