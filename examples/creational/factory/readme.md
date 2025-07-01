# 工厂方法模式

## 简介
工厂方法模式的定义是，将创建对象的逻辑下放给具体的子类工厂，每个工厂只负责一种产品。它可以解决简单工厂模式违反开闭原则的问题。

## 示例
```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()
```