import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        node = queue.popleft()
        for i in range(1, N+1):
            if graph[node][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1

# input
N, M = map(int, input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    y, x = map(int, input().split())
    graph[y][x] = 1
    graph[x][y] = 1

queue = deque()
count = 0
for i in range(1, N+1):
    if not visited[i]:
        count += 1
        queue.append(i)
        visited[i] = 1
        bfs()

print(count)