def fibonacci_memoization(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)

    return memo[n]


def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dp = [0, 1]

    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


n = 10

print("Memoization:", fibonacci_memoization(n))
print("Tabulation:", fibonacci_tabulation(n))