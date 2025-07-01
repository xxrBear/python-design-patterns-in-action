import unittest

from examples.creational.factory.factory import (
    Cat,
    CatFactory,
    Dog,
    DogFactory,
)


class TestAnimalFactory(unittest.TestCase):
    def test_dog_factory_creates_dog(self):
        factory = DogFactory()
        animal = factory.create_animal()
        self.assertIsInstance(animal, Dog)
        self.assertEqual(animal.speak(), "Woof!")

    def test_cat_factory_creates_cat(self):
        factory = CatFactory()
        animal = factory.create_animal()
        self.assertIsInstance(animal, Cat)
        self.assertEqual(animal.speak(), "Meow!")


if __name__ == "__main__":
    unittest.main()
