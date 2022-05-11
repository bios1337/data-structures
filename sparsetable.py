import math

class SparseTable:
    def __init__(self, values):
        self.values = values
        self.n = len(values)
        self.log2 = [0] * (self.n + 1)
        self.P = math.floor(math.log(self.n) / math.log(2))
        self.dp = []
        self.it = []

        for i in range(self.P + 1):
            self.dp.append([0] * self.n)
            self.it.append([0] * self.n)

        for i in range(self.n):
            self.dp[0][i] = values[i]
            self.it[0][i] = i

        for i in range(2, self.n+1):
            self.log2[i] = self.log2[i // 2] + 1
        
        for p in range(1, self.P + 1):
            i = 0
            while i + (1 << p) <= self.n:
                left = self.dp[p-1][i]
                right = self.dp[p-1][i + (1 << (p - 1))]
                self.dp[p][i] = min(left, right)

                if left <= right:
                    self.it[p][i] = self.it[p-1][i]
                else:
                    self.it[p][i] = self.it[p-1][i + (1 << (p-1))]
                
                i += 1


    def queryMin(self, left, right):
        length = right - left + 1
        p = self.log2[length]
        leftValue = self.dp[p][left]
        rightValue = self.dp[p][right - (1 << p) + 1]
        return min(leftValue, rightValue)

    def queryMinIndex(self, left, right):
        length = right - left + 1
        p = self.log2[length]
        leftValue = self.dp[p][left]
        rightValue = self.dp[p][right - (1 << p) + 1]
        if leftValue <= rightValue:
            return self.it[p][left]
        else:
            return self.it[p][right - (1 << p) + 1]


values = [0, 9, 8, -1, -100, 900, 100, -9, -10000, 100000, -1000000]
x = SparseTable(values)
assert x.queryMinIndex(1, 3) == 3
assert x.queryMinIndex(1, 8) == 8
assert x.queryMin(4, 8) == -10000
