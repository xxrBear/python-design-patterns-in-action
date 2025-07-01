import unittest

from examples.creational.sample_factory.sample_factory import AnimalFactory, Cat, Dog


class TestAnimalFactory(unittest.TestCase):
    def test_create_dog(self):
        animal = AnimalFactory.create_animal("dog")
        self.assertIsInstance(animal, Dog)
        self.assertEqual(animal.speak(), "Woof!")

    def test_create_cat(self):
        animal = AnimalFactory.create_animal("cat")
        self.assertIsInstance(animal, Cat)
        self.assertEqual(animal.speak(), "Meow!")

    def test_create_unknown_animal(self):
        with self.assertRaises(ValueError) as context:
            AnimalFactory.create_animal("bird")
        self.assertEqual("Unknown animal type: bird", str(context.exception))


if __name__ == "__main__":
    unittest.main()
