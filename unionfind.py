class UnionFind:

    def __init__(self, size):
        self.size = size
        self.numOfComponents = size
        self.ids = [i for i in range(size)]
        self.sizes = [1] * size

    def find(self, x):
        root = x
        while root != self.ids[root]:
            root = self.ids[root]

        # setting root for each component found in the path
        while x != root:
            next = self.ids[x]
            self.ids[x] = root
            x = next
        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def componentSize(self, x):
        return self.sizes[x]

    def components(self):
        return self.numOfComponents

    def size(self):
        return self.size;
    
    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        if root1 == root2: return

        if self.sizes[root1] < self.sizes[root2]:
            self.sizes[root2] += self.sizes[root1]
            self.ids[root1] = root2
        else:
            self.sizes[root1] += self.sizes[root2]
            self.ids[root2] = root1

        self.numOfComponents -= 1
         

if __name__ == '__main__':
    u = UnionFind(10)
    u.unify(1, 2)
    u.unify(3, 6)
    u.unify(1, 6)
    print(u.connected(1, 7))