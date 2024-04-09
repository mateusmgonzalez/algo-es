class Queue:
    def __init__(self):
        self.items = []
        self.j = 0
        self.n = 0

    def add(self, item):
        self.items[(self.j + self.n) % len(self.items)] = item

        self.n += 1

