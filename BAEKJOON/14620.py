def sol(i, j):
    if cnt == 3:
        return

    if cost[i][j] == 0:
        result += cost[i][j]

# input
n = int(input())
tile = [list(map(int, input().split())) for _ in range(n)]

cost = []
check = []
for i in range(n-2):
    cost.append([])
    check.append([])

for i in range(n-2):
    for j in range(n-2):
        cost[i].append(tile[i+1][j+1] + tile[i+1][j] + tile[i+1][j+2] + tile[i][j+1] + tile[i+2][j+1])
        check[i].append(0)

cnt = 0
result = 0
sol(i, j)