from turtle import left


class AVLTree:

    class Node:
        def __init__(self, value = None):
            self.value = value
            self.right = None
            self.left = None
            self.height = 0
            self.bf = 0

    def __init__(self):
        self.root = None

    def insert(self, value):
        if value is None:
            return False
        
        self.root = self._insert(self.root, value);
        return True

    def _insert(self, node, value):
        if node is None:
             return self.Node(value)
    
        cmp = node.value - value

        if cmp < 0:
            node.right = self._insert(node.right, value)
        else:
            node.left = self._insert(node.left, value)
                  
        self.update(node)
        return self.balance(node)


    def remove(self, value):
        if value is None:
            return False
        
        if self.contains(self.root, value):
            self.root = self._remove(self.root, value);
            return True
        return False

    def _remove(self, node, value):
        if node is None:
            return None
        
        cmp = node.value - value
        if cmp < 0:
            node.right = self._remove(node.right, value)
        elif cmp > 0:
            node.left = self._remove(node.left, value)
        else:
            if node.left is None and node.right is None:
                # deleting leaf node
                node = None
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.digLeft(node.right).value
                node.value = successor
                node.right = self._remove(node.right, successor)

        self.update(node)
        return self.balance(node)


    def digLeft(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left    
        return curr
        

    def includes(self, value):
        return self.contains(self.root, value)

    def contains(self, root, value):
        if root is None:
            return False

        cmp = root.value - value
        if cmp == 0:
            return True
        elif cmp < 0:
            return self.contains(root.right, value)
        else:
            return self.contains(root.left, value)

    def update(self, node):
        if node is None:
            return 
        lh = -1
        rh = -1
        if node.left is not None:
            lh = node.left.height
        
        if node.right is not None:
            rh = node.right.height

        node.height = 1 + max(lh, rh)
        node.bf = rh - lh

    def balance(self, node):
        # left heavy
        if node.bf == -2:
            if node.left.bf <= 0:
                return self.leftLeftCase(node)
            else:
                return self.leftRightCase(node)
            # right heavy
        elif node.bf == 2:
            if node.right.bf <= 0:
                return self.rightRightCase(node)
            else:
                return self.rightLeftCase(node)

        # node is balanced already
        return node


    def leftRotate(self, node):
        parent = node.right
        node.right = parent.left
        parent.left = node
        self.update(node)
        self.update(parent)
        return parent

    def rightRotate(self, node):
        parent = node.left
        node.left = parent.right
        parent.right = node
        self.update(node)
        self.update(parent)
        return parent

    def leftLeftCase(self, node):
        return self.rightRotate(node)

    def rightRightCase(self, node):
        return self.leftRotate(node)

    def leftRightase(self, node):
        node.left = self.leftRotate(node.left)
        return self.leftLeftCase(node)

    def rightLeftCase(self, node):
        node.right = self.rightRotate(node.right)
        return self.rightRightCase(node)

    def printInOrder(self):
        self._printInOrder(self.root)

    def _printInOrder(self, node):
        if node is None:
            return
        self._printInOrder(node.left)
        print(node.value)
        self._printInOrder(node.right)


avl = AVLTree()

avl.insert(100)
avl.insert(1000)
avl.insert(-100)

avl.printInOrder()
print(avl.includes(0))
print(avl.includes(-100))
avl.remove(-100)
print(avl.includes(-100))
avl.insert(100)
avl.insert(1000)
avl.insert(-100)
print('''''''')
avl.printInOrder()


