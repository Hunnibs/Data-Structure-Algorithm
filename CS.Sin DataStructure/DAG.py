import sys
sys.setrecursionlimit(5000)

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

# 입력
n = int(input())
m = int(input())
G = [[] for _ in range(n)]
# G를 입력 받아 처리
for _ in range(m):
	v, w= tuple(map(int, input().split()))
	G[v].append(w)
for i in range(n):
	G[i].sort(reverse=True)

# visited, pre, post 리스트 정의와 초기화
visited = [False for _ in range(n)]
pre = [-1 for _ in range(n)]
post = [-1 for _ in range(n)]
parent = [None for _ in range(n)]
L = []

curr_time = 1

DFSALL(G)

print(' '.join(reversed(L)))