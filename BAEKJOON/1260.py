from collections import deque

def DFS(V):
    result.append(V)
    visited[V] = 1
    for i in range(N+1):
        if arr[V][i] == 1 and visited[i] == 0:
            DFS(i)

def BFS():
    while queue:
        node = queue.popleft()
        result2.append(node)
        for i in range(N+1):
            if arr[node][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1

# input
N, M, V = map(int, input().split())

arr = list([0] * (N+1) for _ in range(N+1))
visited = [0] * (N+1)
visited2 = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

result = []
DFS(V)

result2 = []
visited2[V] = 1
queue = deque()
queue.append(V)
BFS()

for i in range(len(result)):
    if i == len(result)-1:
        print(result[i])
    else:
        print(result[i], end=' ')

for word in result2:
    print(word, end=' ')