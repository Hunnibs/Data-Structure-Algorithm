import sys
sys.setrecursionlimit(10**6)

def check(root):
    for v in node[root]:
        if parent[v] == 0:
            parent[v] = root
            check(v)

# input
input = sys.stdin.readline

N = int(input())

node = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]
parent[1] = 1

for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

check(1)

for i in range(2, N+1):
    print(parent[i])