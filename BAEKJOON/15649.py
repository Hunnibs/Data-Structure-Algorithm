import copy
def sol(num, visited):
    tmp = check(num, visited)
    if :
        for i in range(0,)
        return

    for i in range(N):
        if tmp[i] == 0:
            sol(i+1, tmp)

def check(num, visited):
    tmp = copy.deepcopy(visited)
    tmp[num-1] = num

    return tmp

# input
N, M = map(int, input().split())

visited = [0] * N
result = [0] * M

for i in range(N):
    sol(i+1, visited)
