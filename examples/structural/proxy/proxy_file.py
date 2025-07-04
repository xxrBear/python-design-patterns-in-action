class File:
    def __init__(self, filename):
        self.filename = filename

    def delete(self):
        print(f"{self.filename} deleted.")


# 代理类
class FileProxy:
    def __init__(self, user, file: File):
        self.user = user
        self.file = file

    def delete(self):
        if self.user == "admin":
            self.file.delete()
        else:
            print("Permission denied.")
