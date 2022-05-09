class BST:
    def __init__(self):
        self.root = None

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, root, value):
        if root is None:
            return None
        if root.value == value:
            return root
        elif root.value < value:
            return self._find(root.right, value)
        else:
            return self._find(root.left, value)

    def add(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return self.root
        self._add(self.root, value)
    
    def _add(self, node, value):
        if node is None:
            node = self.Node(value)
        else:
            if node.value < value:
                node.right = self._add(node.right, value)
            else:
                node.left = self._add(node.left, value)

        return node

    def digLeft(self, root):
        while root.left is not None:
            root = root.left
        return root
    
    def digRight(self, root):
        while root.right is not None:
            root = root.right
        return root
    
    def remove(self, value):
        node = self.find(value)
        if node is None:
            return False

        self._remove(self.root, value)
        return True
    
    def _remove(self, root, value):
        if root is None:
            return None
        root_val = root.value
        if root_val > value:
            root.left = self._remove(root.left, value)
        elif root_val < value:
            root.right = self._remove(root.right, value)
        else:
            if root.left is None and root.right is None:
                print('deleting leaf node', root.value)
                root = None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.digLeft(root.right)
                root.value = successor.value
                root.right = self._remove(root.right, successor.value)
                
        return root
            
    
    
    def printInorder(self):
        self.inorder(self.root)
    
    def inorder(self, root):
        if root is None: return
        self.inorder(root.left)
        print(root.value, end=',')
        self.inorder(root.right)

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right


if __name__=='__main__':
    bst = BST()
    bst.add(13)
    bst.add(0)
    bst.add(90)
    bst.add(1010101)
    bst.add(-1)
    bst.remove(0)
    bst.printInorder()
