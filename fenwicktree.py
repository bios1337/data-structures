class FenwickTree:
    def __init__(self,values) -> None:
        vals = values.copy()
        vals.insert(0, 0)
        self.tree = vals

        self.length = len(self.tree)

        # create fenwick tree in linear time
        for i in range(1, self.length):
            j = i + self.lsb(i)
            if j < self.length: 
                self.tree[j] += self.tree[i]

    def lsb(self,num):
        return num & -num;

    def add(self, i, value):
        i += 1
        while i < self.length:
            self.tree[i] += value
            i += self.lsb(i)

    def addRange(self, l, r, value):
        for i in range(l, r + 1):
            self.add(i, value)

    def prefixSum(self, i):
        i += 1
        total = 0
        while i != 0:
            total += self.tree[i]
            i &= ~self.lsb(i)

        return total

    def sum(self, l, r):
        return self.prefixSum(r) - self.prefixSum(l-1)

    def set(self, i, value):
        curr = self.sum(i, i)
        self.add(i, value - curr)

    def print(self):
        for i in range(0, self.length - 1):
            print(self.sum(i, i), end=',')
        print()


if __name__ == '__main__':
    values = [1,2,3,4,5,6,7,8,9,10]
    fenwick = FenwickTree(values)
    fenwick.print()
    fenwick.addRange(0, 5, 1)
    fenwick.print()