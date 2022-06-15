'''
모든 연산은 KN 시간 내에 마칠 수 있다. 즉, O(n)안에 완료 가능하다. 
'''

def preorder(pre, path_sum, A, B, a, path):
    if A[a] == '[]':
        return
    for i in range(len(A[a])):
        pre.append(A[a][i])
        path_sum.append(path+B[A[a][i]])  # 기존 preorder 코드에 경로 합 구하는 파트 추가
        preorder(pre, path_sum, A, B, A[a][i], path+B[A[a][i]])
    
    return pre, path_sum

# 부트리수를 계산해주는 재귀 함수
def subNode_count(subNode, A, a):
    cnt = 1
    for i in range(len(A[a])):
        plus, subNode = subNode_count(subNode, A, A[a][i])
        cnt += plus
    
    subNode[a] = cnt

    return cnt, subNode

# 경로에 있는 노드의 가중치가 업데이트 됐을 때 부트리까지 모두 업데이트
def query_update(pre, path_sum, u, v):
    start = pre.index(u)
    for i in range(subNode[u]):
        path_sum[start] += v
        start += 1

# 경로 합 리스트에 저장해놓은 것을 출력하면 됨
def query_sum(path_sum, pre, v):
    n = pre.index(v)
    
    return path_sum[n]

n, q = map(int, input().split())
B = list(map(int, input().split()))

B.insert(0, -1)  # 해당 노드 번호에 가중치 값을 맞춰주기 위해 인덱스 0에 -1을 추가
A = []
subNode = [-1, n]  # 각 노드 당 부트리 수를 저장해줄 리스트

for i in range(n+1):  # 이차원 리스트 생성
    A.append([])
    
for i in range(n-1):  # 1차원 인덱스에 부모노드 정보, 안에 자식노드 정보를 저장해준다.
    a, b = map(int, input().split())
    A[a].append(b)
    subNode.append(0) 

pre = [1]
path_sum = [B[1]]
a = 1
pre, path_sum = preorder(pre, path_sum, A, B, a, B[1])
cnt, subNode = subNode_count(subNode, A, a)

result = []
# 질의 수만큼 질문을 받아줌
for i in range(q):
    cmd = input().strip().split()
    if cmd[0] == 'sum':
        v = int(cmd[1])
        result.append(query_sum(path_sum, pre, v))
    elif cmd[0] == 'update':
        v = int(cmd[1])
        b = int(cmd[2])
        query_update(pre, path_sum, v, b)
    else:
        print("Try again")
        
for i in range(len(result)):
	print(result[i])