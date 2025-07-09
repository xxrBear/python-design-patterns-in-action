# test_coffee.py

import unittest

from examples.structural.decorator.decorator import Coffee, SugarDecorator


class TestCoffeeDecorator(unittest.TestCase):
    def test_plain_coffee_cost(self):
        coffee = Coffee()
        self.assertEqual(coffee.cost(), 10)

    def test_sugar_coffee_cost(self):
        coffee = Coffee()
        sugar_coffee = SugarDecorator(coffee)
        self.assertEqual(sugar_coffee.cost(), 12)

    def test_double_sugar_coffee_cost(self):
        coffee = Coffee()
        sugar1 = SugarDecorator(coffee)
        sugar2 = SugarDecorator(sugar1)
        self.assertEqual(sugar2.cost(), 14)


if __name__ == "__main__":
    unittest.main()
