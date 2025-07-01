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
