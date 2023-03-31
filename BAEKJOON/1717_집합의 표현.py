import sys

def find(x):
    # root node이면 값 반환
    if parent[x] == x:
        return x

    root = find(parent[x])
    parent[x] = root

    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)

    parent[y] = x

# input
input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    x, a, b = map(int, input().split())

    if x == 0 and parent[a] != parent[b]:
        union(a, b)
    elif x == 1:
        find(a)
        find(b)
        if parent[a] == parent[b]:
            print("YES")
        else:
            print("NO")