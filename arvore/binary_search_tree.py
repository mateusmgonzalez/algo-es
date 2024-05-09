class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.value,
                                    self.value,
                                    self.right and self.right.value)

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def in_order(self):
        def inorder(root):
            if root:
                inorder(root.left)
                print(root.value),
                inorder(root.right)

        inorder(self.root)

    def search(self, k):
        def searchHelper(root, value):
            if root is None or root.value == value:
                return root  # Retornando o nó encontrado
            elif value < root.value:
                return searchHelper(root.left, value)
            else:
                return searchHelper(root.right, value)

        return searchHelper(self.root, k)

    def insert(self, node):
        def insertHelper(root, node):
            if root is None:
                return Node(node.value)
            if node.value < root.value:
                root.left = insertHelper(root.left, node)
            elif node.value > root.value:
                root.right = insertHelper(root.right, node)
            return root  # Retorno desnecessário

        self.root = insertHelper(self.root, node)

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(Node(1))
    tree.insert(Node(3))
    tree.insert(Node(0))
    tree.insert(Node(4))
    tree.insert(Node(3))
    tree.insert(Node(6))
    tree.in_order()

