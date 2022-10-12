'''
리스트에 루트 노드의 정보를 저장한다고 생각하고 union-find 방식을 사용.
Friend 리스트에 아군이 되는 트리의 루트 노드 정보를 기록해주고 Enemy 리스트에는 루트 노드에 맞춰 적의 집단 루트 노드의 정보를 기록해 준다.
각 함수는 
'''
#
# 4개의 연산 함수 코드 등
#
def set_friends(x, y):  # 두 사람 x와 y는 아군 관계로 지정
    if Friend[x] == Friend[y]:  # 이미 아군이라면
        return
    else:  # 아군이 아닌 경우
        a, b = Friend[x], Friend[y]
        if Enemy[a] == Enemy[b]:
            for i in range(n):
                if Friend[i] == b:
                    Friend[i] = a
        else:  # 적이 다를 경우
            if Enemy[a] == -1:  # 한쪽만 적이 있는 경우
                for i in range(n):  # Y쪽에 적이 있는 경우, Y로 소속원 전체 소속 옮겨주기
                    if Friend[i] == a:
                        Friend[i] = b
            elif Enemy[b] == -1:
                for i in range(n):  # X쪽에 적이 있는 경우, X로 소속원 전체 소속 옮겨주기
                    if Friend[i] == b:
                        Friend[i] = a
            else:  # 서로 적이 다를 경우
                for i in range(n):
                    if Friend[i] == a:
                        Friend[i] = b
                for i in range(n):
                    if Friend[i] == Enemy[a]:
                        Friend[i] = Enemy[b]
                Enemy[Enemy[a]] = -1
                Enemy[a] = -1

def set_enemies(x, y):  # 두 사람 x와 y는 적군 관계로 지정
    # 소속 대표
    Ex = Friend[x]
    Ey = Friend[y]

    if Enemy[Ex] == -1 and Enemy[Ey] == -1:  # 두 소속 모두 적이 없는 경우
        Enemy[Ex], Enemy[Ey] = Ey, Ex
    elif Enemy[Ex] == -1 or Enemy[Ey] == -1:  # 둘 중 하나만 적이 있는 경우
        if Enemy[Ex] == -1:  # y는 적이 있는 경우
            set_friends(Enemy[Ey], Ex)
        else:  # x는 적이 있는 경우
            set_friends(Enemy[Ex], Ey)
    else:  # 둘 다 적이 있는 경우
        set_friends(Enemy[Ey], x)
        set_friends(Enemy[Ex], y)

def are_friends(x, y):  # 두 사람 x와 y가 서로 아군이면 True, 아니면 False
    a,b = Friend[x], Friend[y]
    if Enemy[a] == b and Enemy[b] == a:  # 서로 적일 경우
        return False

    if a == b:  # 서로 아군일 경우
        return True
    else:
        return False

def are_enemies(x, y):  # 두 사람 x와 y가 서로 적군이면 True, 아니면 False
    a,b = Friend[x], Friend[y]
    if a == b:  # 서로 아군일 경우
        return False
    
    if Enemy[a] == b and Enemy[b] == a:  # 서로 적일 경우
        return True
    else:
        return False

n = int(input())

#
# 필요한 자료구조 정의
#
# 정보를 저장해 줄 리스트 두 개 생성
Friend = []  # 소속 정보를 저장
Enemy = []  # 적군 정보를 저장
for i in range(n):
    Friend.append(i)  
    Enemy.append(-1)

# 아래 코드는 가능하면 고치지 말 것!
while True:
    query, x, y = input().split()
    x, y = int(x), int(y)
    if query == 'sf':
        if are_enemies(x, y): # conflict, then print -1
            print(-1)
        else:
            set_friends(x, y)
    elif query == 'se':
        if are_friends(x, y):
            print(-1)
        else:
            set_enemies(x, y)
    elif query == 'af':
        if are_friends(x, y):
            print(1)
        else:
            print(0)
    elif query == 'ae':
        if are_enemies(x, y):
            print(1)
        else:
            print(0)
    elif query == 'exit':
        break
    else:
        print('not allowed operation')