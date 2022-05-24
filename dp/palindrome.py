

import sys

def palindromePartition(str) -> int:
    dp = [[-1] * (len(str) + 1) for _ in range(len(str) + 1)]
    res = solve(str, 0, len(str) - 1, dp)
    print(res)
    return res

def isPalindrome(str):
    length = len(str)
    for i in range(length // 2 + 1):
        if str[i] != str[length - i - 1]:
            return False
    return True

def solve(str, i, j, dp):
    if i >= j:
        return 0
    if len(str) <= 1:
        return 0
    if isPalindrome(str[i:j+1]):
        print(str[i:j+1])
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    mn = sys.maxsize
    for k in range(i , j):
        if dp[i][k] == -1:
            dp[i][k] = solve(str, i, k, dp)
        if dp[k+1][j] == -1:
            dp[k+1][j] = solve(str, k+1, j, dp)
        temp = 1 + dp[i][k] + dp[k+1][j]
        mn = min(mn, temp)
    dp[i][j] = mn
    return mn



palindromePartition('nmi878imb')