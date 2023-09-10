class BinNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = BinNode(value)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while True:
                if node.value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        break

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def find_num(self, num):
        return self._find_num_recursive(self.root, num)

    def _find_num_recursive(self, root, num):
        if not root:
            return False
        if root.value == num:
            return True
        else:
            if root.value > num:
                return self._find_num_recursive(root.left, num)
            else:
                return self._find_num_recursive(root.right, num)

    def find_min(self):
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        if not node.left:
            return node.value
        else:
            return self._find_min_recursive(node.left)

    def find_max(self):
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        if not node.right:
            return node.value
        else:
            return self._find_max_recursive(node.right)


tree = BinaryTree()
tree.insert(4)
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(6)

print(tree.find_min())
print(tree.find_max())
print(tree.find_num(5))

print("Inorder Traversal:", tree.inorder_traversal())
print(tree.find_max())
print(tree.find_min())
print(tree.find_num(8))
print(tree.find_num(5))
