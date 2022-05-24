def subset_sum(arr: list[int], sum):
    length = len(arr)
    dp = [[False for _ in range(sum + 1)] for _ in range(length + 1)]
    

    for i in range(length + 1):
        for j in range(sum + 1):
            if j == 0:
                dp[i][j] = True
                continue

            if i == 0:
                dp[i][j] = False
                continue

            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[length][sum]

print(subset_sum([1, 2, 4, 6, 8], 20))