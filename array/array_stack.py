


class ArrayStack:
    def __init__(self):
        self.items = []
        self.size = 0

    def get(self, i):
        return self.items[i]

    def set(self, i, value):
        self.items[i] = value

    def push(self, item):
        # if self.size == len(self.items):
        #     self.resize()

        self.items.append(item)
        self.size += 1

    def remove(self, i):
        x = self.items[i]
        self.items.pop(i)
        self.size -= 1
        # if len(self.items) >= 3 * self.size:
        #     self.resize()
        return x

    # def resize(self):
    #     b = max(1, 2 * self.size)
    #     for i in range(b):

