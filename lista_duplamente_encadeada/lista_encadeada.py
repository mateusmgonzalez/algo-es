class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None


class ListaEncadeada:
    def __init__(self, head=None, tail=None):
        self.n = 0
        self.head = head
        self.tail = tail

    def push(self, valor):
        u = Node(valor)
        u.next = self.head
        self.head = u
        if self.n == 0:
            self.tail = u
        self.n += 1
        return valor

    def pop(self):
        if self.n == 0:
            return None

        x = self.head.valor
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None

        return x

    def __str__(self):
        if self.n == 0:
            return "[]"

        current = self.head
        values = []
        while current:
            values.append(str(current.valor))
            current = current.next

        return f"[Head: {str(self.head.valor)}, Tail: {str(self.tail.valor)}, Values: {', '.join(values)}]"

    def remove(self):
        return self.pop()

    def add(self, x):
        u = Node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u

        self.tail = u
        self.n += 1
        return True


if __name__ == '__main__':
    lista1 = ListaEncadeada()
    lista1.push(1)
    lista1.push(2)
    lista1.push(3)
    lista1.push(4)
    lista1.push(5)
    lista1.push(6)
    lista1.push(7)
    lista1.push(8)
    lista1.push(9)
    lista1.push(10)
    lista1.pop()
    lista1.pop()
    lista1.pop()

    queueLinkada = ListaEncadeada()
    queueLinkada.add(1)
    queueLinkada.add(2)
    queueLinkada.add(3)
    queueLinkada.add(4)
    queueLinkada.add(5)
    queueLinkada.pop()
    queueLinkada.pop()


    print(queueLinkada)
