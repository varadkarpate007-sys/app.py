import random

rows = 5
cols = 5

grid = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 9))
    grid.append(row)

blocked = [(1, 2), (3, 1)]
delayed = [(2, 3)]

for i, j in delayed:
    grid[i][j] += 10

for i, j in blocked:
    grid[i][j] = -1

print("Grid:")

for row in grid:
    print(row)

dp = [[float("inf")] * cols for _ in range(rows)]

parent = [[None] * cols for _ in range(rows)]

dp[0][0] = grid[0][0]

for i in range(rows):
    for j in range(cols):

        if grid[i][j] == -1:
            continue

        if i == 0 and j == 0:
            continue

        if i > 0 and dp[i - 1][j] != float("inf"):
            if dp[i - 1][j] + grid[i][j] < dp[i][j]:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
                parent[i][j] = (i - 1, j)

        if j > 0 and dp[i][j - 1] != float("inf"):
            if dp[i][j - 1] + grid[i][j] < dp[i][j]:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
                parent[i][j] = (i, j - 1)

path = []

i = rows - 1
j = cols - 1

if dp[i][j] == float("inf"):
    print("No path available")
else:
    while (i, j) != (0, 0):
        path.append((i, j))
        i, j = parent[i][j]

    path.append((0, 0))
    path.reverse()

    print("\nOptimal Total Time:", dp[rows - 1][cols - 1])
    print("Optimal Path:", path)