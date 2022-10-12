'''
모든 연산은 KN 시간 내에 마칠 수 있다. 즉, O(n)안에 완료 가능하다.
'''

import sys  # 재귀의 깊이가 깊어질 경우 해결하지 못하는 오류가 발생하여 추가
sys.setrecursionlimit(10**9)

def dfs(depth, parent, A, a, d):
    depth[a] = d  # 깊이 정보를 저장
    for i in range(len(A[a])):
        parent[A[a][i]] = a  # 부모노드 정보를 저장
        dfs(depth, parent, A, A[a][i], d+1)


def lca(a, b):
    # 깊이 정보를 둘이 같게 맞춰줌
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 같은 깊이에서 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

n, q = map(int, input().split())

A = []
depth = [0] * (n+1)
parent = [0] * (n+1)
for i in range(n+1):  # 이차원 리스트 생성
    A.append([])
    
for i in range(n-1):  # 1차원 인덱스에 부모노드 정보, 안에 자식노드 정보를 저장해준다.
    a, b = map(int, input().split())
    A[a].append(b)

dfs(depth, parent, A, 1, 0)

result = []
for i in range(q):
    a, b = map(int, input().split())
    result.append(lca(a, b))

for i in range(len(result)):
	print(result[i])