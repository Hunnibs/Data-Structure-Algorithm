import copy

def sol(num, visited, result):
    tmp_arr, tmp_result = check(num, visited, result)

    if len(tmp_result) == M:
        for num in tmp_result:
            print(num, end=' ')
        print()
        return

    for i in range(N):
        if tmp_arr[i] == False:
            sol(i+1, tmp_arr, tmp_result)

def check(num, visited, result):
    tmp = copy.deepcopy(visited)
    result = copy.deepcopy(result)

    tmp[num-1] = True
    result.append(num)

    return tmp, result

# input
N, M = map(int, input().split())

result = []
visited = [False] * N
for i in range(N):
    sol(i+1, visited, result)
