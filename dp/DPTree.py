def calculateDiameter(root):
    if root is None:
        return 0

    res = [0]
    solve(root, res)

    return res[0]

def solve(root, res):
    if root is None:
        return 0

    # hypothesis
    left = solve(root.left, res)
    right = solve(root.right, res)
    temp = 1 + max(left, right)
    ans = left + right
    res[0] = max(res[0], ans)

    return temp
    

class Node:

    def __init__(self):
        self.left = None
        self.right = None

n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()
n6 = Node()
n7 = Node()
n8 = Node()
n9 = Node()


n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n7
n7.right = n8
n8.right = n9
n4.left = n5
n5.right = n6

print(calculateDiameter(n1))