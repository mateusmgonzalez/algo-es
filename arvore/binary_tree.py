class BinaryTree:
    def __init__(self, value):
        self.tree = {'value': value, 'left': None, 'right': None}

    def insert(self, value):
        self._insert_recursive(self.tree, value)

    def _insert_recursive(self, node, value):
        if value < node['value']:
            if node['left'] is None:
                node['left'] = {'value': value, 'left': None, 'right': None}
            else:
                self._insert_recursive(node['left'], value)
        elif value > node['value']:
            if node['right'] is None:
                node['right'] = {'value': value, 'left': None, 'right': None}
            else:
                self._insert_recursive(node['right'], value)

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.tree)

    def _inorder_traversal_recursive(self, node):
        if node:
            self._inorder_traversal_recursive(node['left'])
            print(node['value'])
            self._inorder_traversal_recursive(node['right'])

if __name__ == '__main__':
    # Exemplo de uso:
    tree = BinaryTree(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print("Inorder traversal da árvore binária:")
    tree.inorder_traversal()
