import warnings
class LinkedList:
    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next= self.tail
        self.tail.prev = self.head
        self.elements = 0

    def print(self):
        curr = self.head.next
        while curr.next != None:
            print(curr.value, end=',')
            curr = curr.next

    def appendIndex(self, index, value):
        warnings.warn('appendIndex is deprecated', DeprecationWarning)
        curr = self.head
        currIndex = -1
        while currIndex != index:
            curr = curr.next
            currIndex += 1
            if curr.next is None:
                raise Exception('out of range')
        
        node = self.Node()
        node.value = value
        prev = curr.prev
        prev.next = node
        node.next = curr
        curr.prev = node
        node.prev = prev
        self.elements += 1
    
    def appendRight(self, value):
        tail = self.tail
        prev = tail.prev
        node = self.Node()
        node.value = value
        prev.next = node
        node.next = tail
        tail.prev = node
        node.prev = prev
        self.elements += 1

    def appendLeft(self, value):
        head = self.head
        head_next = head.next
        node = self.Node()
        node.value = value
        head_next.prev = node
        node.next = head_next
        head.next= node
        node.prev = head
        self.elements += 1

    def popIndex(self, index):
        curr = self.head
        currIndex = -1
        while currIndex != index:
            curr = curr.next
            currIndex += 1
            if curr.next is None:
                raise Exception('out of range')
        nodeToRemove = curr
        prev = curr.prev
        next = curr.next
        prev.next = next
        next.prev = prev
        self.elements -= 1
        return nodeToRemove.value
    
    def popLeft(self):
        return self.popIndex(0)

    def popRight(self):
        tail = self.tail
        if tail.prev.prev is None:
            raise Exception('list is already empty')

        nodeToRemove = tail.prev
        prev = nodeToRemove.prev
        next = nodeToRemove.next
        prev.next = next
        next.prev = prev
        self.elements -= 1
        return nodeToRemove.value
    
    def top(self):
        last = self.tail.prev
        if last.prev is None:
            raise Exception('list is empty')
        return last.value

    def size(self):
        return self.elements

    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None


if __name__ == '__main__':
    ll = LinkedList()
    ll.appendLeft(1)
    ll.appendRight(0)
    ll.appendLeft(3)
    ll.appendRight(5)
    ll.appendLeft(7)
    ll.appendRight(9)
    ll.print()
    ll.appendIndex(1, 8)
    ll.print()
    ll.popIndex(2)
    ll.print()
    ll.popIndex(2)
    ll.print()
    ll.popLeft()
    ll.print()
    ll.popRight()
    ll.print()
