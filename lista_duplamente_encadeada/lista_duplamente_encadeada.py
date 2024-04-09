class Node:

    def __init__(self, prev=None, next=None, data: int = None):
        self.prev = prev
        self.next = next
        self.data = data


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.n = 0
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, i):
        if i < self.n / 2:
            p = self.dummy.next
            for j in range(1, i):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n - i):
                p = p.prev
        return p

    def get(self, i):
        return self.get_node(i).data

    def set(self, i, x):
        u = self.get_node(i)
        y = u.data
        u.data = x
        return y

    def add_before(self, w, x):
        u = Node(data=x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i, x):
        self.add_before(self.get_node(i), x)

    def remove_node(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def remove(self,i):
        self.remove_node(self.get_node(i))