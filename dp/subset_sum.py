def calculateSubsetSum(arr, sum):
    return solve(arr, len(arr), sum)


def solve(arr, n, target): 
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(target + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i][j - 1]

    return dp[n][target]

print(calculateSubsetSum([3, 1, 3], 4))
