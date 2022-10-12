'''
이차원리스트를 활용, 각 노드 번호를 인덱스에 맞춰주고 자식노드들을 저장해준다. 이후 preorder와 postorder 함수를 통해 정렬해주고 문제의 조건에 따라 해결함
시간복잡도는 처음 이차원리스트 생성 시 n, 재귀함수가 각각 n, n, 그리고 질의는 q만에 가능하므로 총 3qn 시간 만에 가능하므로 총 O(n)시간에 가능하다. 
'''

import sys  # 재귀의 깊이가 깊어질 경우 해결하지 못하는 오류가 발생하여 추가
sys.setrecursionlimit(10**9)

def preorder(pre, A, a):
    if A[a] == '[]':
        return
    for i in range(len(A[a])):
        pre.append(A[a][i])
        preorder(pre, A, A[a][i])
        
    return pre

def postorder(post, A, a):
    if A[a] == '[]':
        return
    for i in range(len(A[a])):
        postorder(post, A, A[a][i])
        post.append(A[a][i])
        
    return post

def query_ancestor(pre, post, u, v):
    if u == v:
        return True
    elif pre.index(u) < pre.index(v) and post.index(u) > post.index(v):
        return True
    else:
        return False
    
# 트리 생성
n, q = map(int, input().split())

A = []
for i in range(n+1):  # 이차원 리스트 생성
    A.append([])
    
for i in range(n-1):  # 1차원 인덱스에 부모노드 정보 , 안에 자식노드 정보를 저장해준다.
    a, b = map(int, input().split())
    A[a].append(b)

# preorder, postorder로 정렬    
pre, post = [1], []
a = 1
pre = preorder(pre, A, a)
post = postorder(post, A, a)
post.append(1)

cnt = 0

# 질의 구문
for i in range(q):
    u, v = map(int, input().split())
    if query_ancestor(pre, post, u, v) == True:
        cnt += 1
    
print(cnt)