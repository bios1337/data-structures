def count_subset_sum(arr: list[int], target: int):
    length = len(arr)
    dp = [[0] * (target + 1) for _ in range(length + 1)]

    for i in range(length + 1):
        for j in range(target + 1):
            if j == 0:
                dp[i][j] = 1
                continue

            if i == 0:
                dp[i][j] = 0
                continue

            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[length][target]

print(count_subset_sum([1,2,3,3], 6))
print(count_subset_sum([1,1,1,1], 1))
