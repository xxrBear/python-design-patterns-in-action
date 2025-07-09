# 抽象组件
class FileSystemItem:
    def show(self, indent=0):
        raise NotImplementedError


# 叶子节点：文件
class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"- 文件：{self.name}")


# 组合节点：文件夹
class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def show(self, indent=0):
        print(" " * indent + f"+ 文件夹：{self.name}")
        for child in self.children:
            child.show(indent + 4)


if __name__ == "__main__":
    root = Folder("根目录")
    root.add(File("README.md"))
    root.add(File("main.py"))

    subfolder = Folder("图片")
    subfolder.add(File("cat.jpg"))
    subfolder.add(File("dog.png"))

    root.add(subfolder)
    root.show()
