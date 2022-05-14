
# knapsack
def calculateMaxProfit(weights, values, W):
    N = len(weights)
    return knapsack(weights, values, W, N);

def knapsack(weights, values, W, N):
    if W == 0 or N == 0:
        return 0

    if weights[N - 1] <= W:
        return max(values[N-1] + knapsack(weights, values, W - weights[N - 1], N - 1), knapsack(weights, values, W, N-1))
    else:
        return knapsack(weights, values, W, N-1)
    
print(calculateMaxProfit([1, 2, 3, 4], [10, 1, 5, 0], 1))

