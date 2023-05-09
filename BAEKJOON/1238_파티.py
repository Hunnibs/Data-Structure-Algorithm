import heapq
import sys
from math import inf

def dijkstra(i, shortPath):
    heap = []
    heapq.heappush(heap, (0, i))
    while heap:
        currentW, currentV = heapq.heappop(heap)

        for nextV, w in graph[currentV]:
            nextW = currentW + w
            if shortPath[nextV] > nextW:
                shortPath[nextV] = nextW
                heapq.heappush(heap, (nextW, nextV))

    return shortPath

# input
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# main
result = [0 for _ in range(N+1)]

shortPathX = [inf for _ in range(N+1)]
shortPathX[X] = 0
shortPathX = dijkstra(X, shortPathX)

for i in range(1, N+1):
    if i == X:
        continue

    shortPath = [inf for _ in range(N+1)]
    shortPath[i] = 0
    shortPath = dijkstra(i, shortPath)
    result[i] = shortPath[X] + shortPathX[i]

print(max(result))