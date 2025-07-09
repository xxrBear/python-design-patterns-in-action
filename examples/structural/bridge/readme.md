# 桥接模式

## 简介
桥接模式是一种结构型设计模式，目的是将抽象部分与实现部分分离，使它们可以独立变化。

## 示例
```python
# 实现接口：消息发送方式
class MessageSender:
    def send(self, message):
        raise NotImplementedError()

class EmailSender(MessageSender):
    def send(self, message):
        print(f"用邮件发送消息: {message}")

class SMSSender(MessageSender):
    def send(self, message):
        print(f"用短信发送消息: {message}")

# 抽象类：消息
class Message:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send(self, message):
        self.sender.send(message)

# 扩展抽象：紧急消息
class UrgentMessage(Message):
    def send(self, message):
        self.sender.send(f"[紧急] {message}")
```