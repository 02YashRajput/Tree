class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor
            root.key = self._min_value_node(root.right).key

            # Delete the inorder successor
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        result = []
        if root:
            result += self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

    def preorder_traversal(self, root):
        result = []
        if root:
            result.append(root.key)
            result += self.preorder_traversal(root.left)
            result += self.preorder_traversal(root.right)
        return result
    
    def postorder_traversal(self, root):
        result =[]
        if root:
            result += self.postorder_traversal(root.left)
            result += self.postorder_traversal(root.right)
            result.append(root.key)
        return result
            



bst = BST()
a = [10,5,60,20,80,70,65,100]
for i in a:
    bst.insert(i)


print(bst.inorder_traversal(bst.root))
print(bst.preorder_traversal(bst.root))
bst.delete(80)
print(bst.inorder_traversal(bst.root))
print(bst.postorder_traversal(bst.root))
