import copy

def sol(num, result):
    tmp_result = copy.deepcopy(result)

    if len(tmp_result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(N):
        tmp_result.append(num)
        sol(i+1, tmp_result)

# input
N, M = map(int, input().split())

result = []
for i in range(N):
    sol(i+1, result)
