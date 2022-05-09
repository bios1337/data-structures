
from linkedlist import LinkedList


class HashTableSC:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = [None] * self.capacity
        self.items = 0

    def hash(self, key):
        return (key) % self.capacity

    def put(self, key, value):
        hash = self.hash(key)
        
        if not self.hashtable[hash]:
            ll = LinkedList()
            ll.appendRight((key, value))
            self.hashtable[hash] = ll
        else:
            ll = self.hashtable[hash]
            node = self.search(ll, key)
            if node:
                node.value = (key, value)
            else:
                ll.appendRight((key, value))

    def search(self, ll, key):
        curr = ll.head.next
        while curr.next != None:
            if curr.value[0] == key:
                return curr
            curr = curr.next
        return None

    def get(self, key):
        hash = self.hash(key)

        if self.hashtable[hash]:
            ll = self.hashtable[hash]
            node = self.search(ll, key)
            if node:
                return node.value[1]
        
        return None

    def print(self):
        for i in range(self.capacity):
            if self.hashtable[i]:
                print(i, self.hashtable[i].print())
            else:
                print(i, self.hashtable[i])

if __name__ == '__main__':
    ht = HashTableSC(8)
    ht.put(9, 9)
    ht.put(9, 0)
    ht.put(8, 10)
    ht.put(0, 0)
    ht.put(4, 4)
    ht.put(9, 9)
    ht.put(8, 8)
    ht.put(7, 7)
    ht.put(5, 5)

    print(ht.get(9))
    ht.print()

