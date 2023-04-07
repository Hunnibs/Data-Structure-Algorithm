import copy


def solution(arr):
    answer = [0, 0]
    dx = [1, 1, 0, 0]
    dy = [0, 1, 1, 0]

    n = len(arr[0])
    while n > 1:
        next = [[] for _ in range(n // 2)]
        for x in range(0, n, 2):
            for y in range(0, n, 2):
                if arr[x][y] != 2 and arr[x][y] == arr[x + dx[0]][y + dy[0]] and arr[x][y] == arr[x + dx[1]][y + dy[1]] and arr[x][y] == arr[x + dx[2]][y + dy[2]]:
                    next[x // 2].append(arr[x][y])
                else:
                    for i in range(4):
                        if arr[x + dx[i]][y + dy[i]] != 2:
                            answer[arr[x + dx[i]][y + dy[i]]] += 1
                    next[x // 2].append(2)

        arr = copy.deepcopy(next)
        n = n // 2

    if arr[0][0] == 1:
        answer[1] += 1
    elif arr[0][0] == 0:
        answer[0] += 1

    return answer