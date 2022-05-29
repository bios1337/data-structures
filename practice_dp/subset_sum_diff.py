import sys


def subset_sum_difference(arr: list[int]):
    total = sum(arr)
    length = len(arr)
    dp = [[False for _ in range(total + 1)] for _ in range(length + 1)]

    for i in range(length + 1):
        for j in range(total + 1):
            if j == 0:
                dp[i][j] = 1
                continue
            if i == 0:
                dp[i][j] = 0
                continue

            if arr[i - 1] <= j:
                dp[i][j] = dp[i-1][j - arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    
    mn = sys.maxsize
    for i in range(total // 2, -1, -1):
        if dp[length][i]:
            mn = min(mn, total - 2 * i)

    return mn

print(subset_sum_difference([1,1,1,1,1]))

