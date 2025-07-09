import sys
import unittest
from io import StringIO

from examples.structural.composite.composite import File, Folder


class TestFileSystemStructure(unittest.TestCase):
    def setUp(self):
        # 构建测试用的文件结构
        self.root = Folder("根目录")
        self.root.add(File("a.txt"))
        self.root.add(File("b.md"))

        images = Folder("images")
        images.add(File("cat.jpg"))

        self.root.add(images)

    def test_structure_output(self):
        # 捕获打印输出
        captured_output = StringIO()
        sys.stdout = captured_output  # 重定向 stdout

        self.root.show()

        sys.stdout = sys.__stdout__  # 恢复 stdout
        output = captured_output.getvalue()

        expected_output = (
            "+ 文件夹：根目录\n"
            "    - 文件：a.txt\n"
            "    - 文件：b.md\n"
            "    + 文件夹：images\n"
            "        - 文件：cat.jpg\n"
        )

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
