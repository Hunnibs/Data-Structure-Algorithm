'''
위상정렬을 활용하지 못하고 정점으로부터 정점까지 최대거리를 구하는 방식으로 문제 해결, Sink 노드는 추려낼 수 있지만 Source노드는 그렇지 못함
시간 복잡도의 경우 최악의 경우 O(n^2)까지 걸릴 수 있다. 
'''

import sys  # 재귀의 깊이가 깊어질 경우 해결하지 못하는 오류가 발생하여 추가
sys.setrecursionlimit(10**9)

def DFS(G, v):
	global curr_time  # pre, post를 위한 time stamp
	# 그래프 G의 노드 v를 DFS 방문한다
	visited[v] = True
	pre[v] = curr_time
	curr_time += 1
	for w in G[v]:
		if not visited[w]:
			parent[w] = v
			DFS(G, w)
	L.append(str(v))
	post[v] = curr_time
	curr_time += 1

def DFSALL(G):
	# 그래프 G를 DFS 방문한다
	for v in range(n-1, -1, -1):
		if visited[v] == False:
			DFS(G,v)

def LongestPath(start, destination):  # 어느 한 점부터 목적지까지 
	start, destination = int(start), int(destination)
	if start == destination:
		return
	for w in G[start]:
		LongestPath(w, destination)
		D[start] = max(D[start], D[w] + W[str(start) + str(w)])

	return max(D)

# 입력
n = int(input())
m = int(input())
G = [[] for _ in range(n)]
W = {}  # 가중치 값을 위해 딕셔너리 자료형 활용
D = [0 for _ in range(n)]  # 최장거리 구하기 위한 리스트 생성
# G를 입력 받아 처리
for _ in range(m):
	v, w, d= tuple(map(int, input().split()))
	G[v].append(w)
	W[str(v) + str(w)] = d
for i in range(n):
	G[i].sort(reverse=True)
# Sink 노드 구해주는 함수 추가
Sink = []
for i in range(n):
	if G[i] == []:
		Sink.append(i)
# visited, pre, post 리스트 정의와 초기화
visited = [False for _ in range(n)]
pre = [-1 for _ in range(n)]
post = [-1 for _ in range(n)]
parent = [None for _ in range(n)]
L = []

curr_time = 1

DFSALL(G)
L.reverse()
Max = 0
for w in Sink:
	ind = L.index(str(w))
	for i in range(ind):
		Max = max(Max, LongestPath(L[i], L[ind]))
print(Max)