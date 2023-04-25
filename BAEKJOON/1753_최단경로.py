import math
import sys
import heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, K))
    while heap:
        currentWeight, currentVertex = heapq.heappop(heap)

        for nextVertex, weight in graph[currentVertex]:
            nextWeight = currentWeight + weight
            if answer[nextVertex-1] > nextWeight:
                answer[nextVertex-1] = nextWeight
                heapq.heappush(heap, (nextWeight, nextVertex))

# input
input = sys.stdin.readline
inf = math.inf

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# main
answer = [inf for _ in range(V)]
answer[K-1] = 0  # 시작점은 0으로 출력
dijkstra()

for i in range(V):
    if answer[i] != inf:
        print(answer[i])
    else:
        print("INF")