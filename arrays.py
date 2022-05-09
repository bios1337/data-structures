class MyArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentIndex = -1
        self.arr = [-1] * capacity

    def get(self, idx):
        if idx < 0 or idx > self.currentIndex:
            raise Exception('cannot access at idx', idx)
        return self.arr[idx]

    def checkAndResize(self):
        if self.currentIndex >= self.capacity:
            self.capacity *= 2
            new_arr = [-1] * self.capacity
            for i in range(len(self.arr)):
                new_arr[i] = self.arr[i]

            self.arr = new_arr

    def len(self):
        return self.capacity

    def appendToEnd(self, element):
        self.currentIndex += 1
        self.checkAndResize()
        self.arr[self.currentIndex] = element

    def appendToIndex(self, index, element):
        self.currentIndex += 1
        self.checkAndResize()
        if index > self.currentIndex:
            raise Exception('cannot append away from array')

        for i in range(self.len() - 1, index, -1):
            self.arr[i] = self.arr[i - 1] 

        self.arr[index] = element

    def appendToFirst(self, element):
        self.appendToIndex(0, element)

    def popRight(self):
        if self.currentIndex < 0:
            raise Exception('cannot pop from empty arr')
        elem = self.arr[self.currentIndex - 1]
        self.arr[self.currentIndex - 1] = -1
        self.currentIndex -= 1
        return elem
    
    def popLeft(self):
        return self.popFromIndex(0)

    def popFromIndex(self, idx):
        elem = self.arr[idx]
        for i in range(idx, self.len() - 1):
            self.arr[i] = self.arr[i + 1]
        return elem

    def printArr(self):
        print(self.arr)


new_arr = MyArray(5)
new_arr.appendToEnd(3)
new_arr.appendToFirst(1)
new_arr.appendToFirst(1)

new_arr.printArr()

new_arr.appendToFirst(4)
new_arr.appendToFirst(5)
new_arr.appendToFirst(6)

new_arr.appendToFirst(7)

new_arr.appendToFirst(8)

new_arr.appendToFirst(9)


x = new_arr.popLeft()
print(x)
new_arr.printArr()

x = new_arr.get(9)
print(x)
new_arr.printArr()