import unittest

from examples.behavioral.memento.memento import Editor, History


class TestMementoPattern(unittest.TestCase):
    def setUp(self):
        self.editor = Editor()
        self.history = History()

    def test_typing_and_saving(self):
        self.editor.type("Hello")
        self.assertEqual(self.editor.get_content(), "Hello")

        self.history.push(self.editor.save())

        self.editor.type(" World")
        self.assertEqual(self.editor.get_content(), "Hello World")

        self.history.push(self.editor.save())

        self.editor.type("!!!")
        self.assertEqual(self.editor.get_content(), "Hello World!!!")

    def test_undo_once(self):
        self.editor.type("Hello")
        self.history.push(self.editor.save())

        self.editor.type(" World")
        self.history.push(self.editor.save())

        self.editor.type("!!!")

        self.editor.restore(self.history.pop())
        self.assertEqual(self.editor.get_content(), "Hello World")

    def test_undo_twice(self):
        self.editor.type("Hello")
        self.history.push(self.editor.save())

        self.editor.type(" World")
        self.history.push(self.editor.save())

        self.editor.type("!!!")

        self.editor.restore(self.history.pop())
        self.editor.restore(self.history.pop())
        self.assertEqual(self.editor.get_content(), "Hello")


if __name__ == "__main__":
    unittest.main()
