def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


def knapsack_top_down(values, weights, W, n, memo={}):
    if n == 0 or W == 0:
        return 0

    if (n, W) in memo:
        return memo[(n, W)]

    if weights[n - 1] > W:
        result = knapsack_top_down(values, weights, W, n - 1, memo)
    else:
        include = values[n - 1] + knapsack_top_down(
            values, weights, W - weights[n - 1], n - 1, memo
        )

        exclude = knapsack_top_down(values, weights, W, n - 1, memo)

        result = max(include, exclude)

    memo[(n, W)] = result
    return result


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Bottom-Up:", knapsack_bottom_up(values, weights, W))

print("Top-Down:", knapsack_top_down(values, weights, W, len(values)))