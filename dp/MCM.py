



import sys


def calculateMinCost(arr):
    if len(arr) in [0, 1]:
        return 0
    ans = solve(arr, 1, len(arr) - 1);
    return ans

def solve(arr, i, j):
    #base
    if i >= j:
        return 0

    mn = sys.maxsize

    for k in range(i, j):
        #hypothesis
        ans = solve(arr, i, k) + solve(arr, k+1, j) + arr[i - 1] * arr[k] * arr[j]

        #induction
        mn = min(mn, ans)
        

    return mn

print(calculateMinCost([10, 20, 30, 10]))

'''
10 * 20
20 * 30
30 * 10

10 * 20 * 30 => 6000 + 10 * 30 * 10 => 6000 + 3000 => 9000
20 * 30 * 10 => 6000 , 10 * 20 * 20 * 10 => 6000 + 

6000 + 30 * 10 * 30 => 9000 + 6000 => 15000

10 * 20 * 30 => 6000
'''



    
