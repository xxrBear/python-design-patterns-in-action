import unittest
from unittest.mock import MagicMock

from examples.behavioral.vistor.state import Engineer, Manager


class TestVisitorPatternElements(unittest.TestCase):
    def test_engineer_accept_calls_visit_engineer(self):
        engineer = Engineer("Alice", 10000)
        visitor = MagicMock()

        engineer.accept(visitor)

        visitor.visit_engineer.assert_called_once_with(engineer)

    def test_manager_accept_calls_visit_manager(self):
        manager = Manager("Bob", 20000, 5000)
        visitor = MagicMock()

        manager.accept(visitor)

        visitor.visit_manager.assert_called_once_with(manager)


if __name__ == "__main__":
    unittest.main()
