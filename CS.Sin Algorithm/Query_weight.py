'''
모든 연산은 KN 시간 내에 마칠 수 있다. 첫 번째 함수는 재귀함수로 N, 두번째 함수도 재귀함수로 N, query_subtree 최악의 경우 2N, query_update는 최악의 경우 N, 나머지 모든 입력, 리스트 생성도 최악의 경우 N시간을 넘어가지 않기 때문에 총 KN 즉 O(n) 시간 내에 가능하다. 
'''

'''
# 재귀의 깊이가 깊어질 경우 해결하지 못하는 오류가 발생할 경우 추가
import sys  
sys.setrecursionlimit(10**9)
'''
# preorder, weight(cost) 리스트를 만들어주는 함수
def preorder(pre, weight, A, B, a):  
    if A[a] == '[]':
        return
    for i in range(len(A[a])):
        pre.append(A[a][i])
        weight.append(B[A[a][i]])
        preorder(pre, weight, A, B, A[a][i])
        
    return pre, weight

# 부트리수를 계산해주는 함수
def subNode_count(subNode, A, a):
    cnt = 1
    for i in range(len(A[a])):
        plus, subNode = subNode_count(subNode, A, A[a][i])
        cnt += plus
    
    subNode[a] = cnt

    return cnt, subNode

# subtree weight 
def query_subtree(pre, weight, subNode, u):
    cnt = 0
    start = pre.index(u)
    for i in range(subNode[u]):
        cnt += weight[start]
        start += 1

    return cnt

# update
def query_update(pre, weight, u, v): 
    weight[pre.index(u)] += v

# 입력 파트
n, q = map(int, input().split())
B = list(map(int, input().split()))

#필요한 리스트 생성
B.insert(0, -1)  # 해당 노드 번호에 가중치 값을 맞춰주기 위해 인덱스 0에 -1을 추가

A = []
subNode = [-1, n]  # 각 노드 당 부트리 수를 저장해줄 리스트
for i in range(n+1):  # 이차원 리스트 생성
    A.append([])
    
for i in range(n-1):  # 1차원 인덱스에 부모노드 정보, 안에 자식노드 정보를 저장해준다.
    a, b = map(int, input().split())
    A[a].append(b)
    subNode.append(0) 

pre, weight = [1], [B[1]]
a = 1
pre, weight = preorder(pre, weight, A, B, a)
cnt, subNode = subNode_count(subNode, A, a)

result = []

# 질의 수만큼 질문을 받아줌
for i in range(q):
    cmd = input().strip().split()
    if cmd[0] == 'subtree':
        v = int(cmd[1])
        result.append(query_subtree(pre, weight, subNode, v))
    elif cmd[0] == 'update':
        v = int(cmd[1])
        b = int(cmd[2])
        query_update(pre, weight, v, b)
    else:
        print("Try again")

for i in range(len(result)):
	print(result[i])