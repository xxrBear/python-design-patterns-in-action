import unittest

from examples.creational.builder.builder import Computer, ComputerBuilder


class TestComputerBuilder(unittest.TestCase):
    def test_build_computer(self):
        builder = ComputerBuilder()
        computer = (
            builder.with_cpu("Intel i7")
            .with_memory("16GB")
            .with_disk("512GB SSD")
            .build()
        )

        self.assertEqual(computer.cpu, "Intel i7")
        self.assertEqual(computer.memory, "16GB")
        self.assertEqual(computer.disk, "512GB SSD")
        self.assertIsInstance(computer, Computer)

    def test_partial_build(self):
        builder = ComputerBuilder()
        computer = builder.with_cpu("AMD Ryzen 5").build()

        self.assertEqual(computer.cpu, "AMD Ryzen 5")
        self.assertIsNone(computer.memory)
        self.assertIsNone(computer.disk)


if __name__ == "__main__":
    unittest.main()
