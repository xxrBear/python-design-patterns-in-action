# 备忘录模式 

## 简介
备忘录模式是一种行为型设计模式，用于在不破坏对象封装的前提下，捕获并保存对象的内部状态，以便在将来将对象恢复到之前的状态。


## 示例
```python
# 发起人：保存当前状态 & 创建备忘录
class Editor:
    def __init__(self):
        self._content = ""

    def type(self, text: str):
        self._content += text

    def get_content(self):
        return self._content

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_state()


# 备忘录：保存状态
class Memento:
    def __init__(self, content: str):
        self._content = content

    def get_state(self):
        return self._content


# 管理者：只保存备忘录对象
class History:
    def __init__(self):
        self._mementos = []

    def push(self, memento: Memento):
        self._mementos.append(memento)

    def pop(self):
        return self._mementos.pop()
```