import copy
import sys
from math import inf

# input
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[inf for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

# main
for K in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][K] + graph[K][j])

for i in range(n):
    graph[i][i] = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == inf:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()