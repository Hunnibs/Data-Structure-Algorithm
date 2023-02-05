import copy

def BackTracking(dx, arr):
    global cnt

    if dx == N-1:  # 마지막 줄일 때
        for i in range(N):
            if arr[dx][i] == 0:
                cnt += 1
        return

    if min(arr[dx]) == 1:
        return

    for i in range(N):
        if arr[dx][i] == 0:
            tmp = visit(dx, i, arr)
            BackTracking(dx+1, tmp)

def visit(dx, dy, arr):  # 체스판 상 놓을 수 없는 위치 업데이트
    tmp = copy.deepcopy(arr)
    if tmp[dx][dy] == 0:
        for i in range(1, N-dx):
            tmp[dx+i][dy] = 1  # 세로
            # 왼쪽 아래 대각
            if 0 <= dy-i < N:
                tmp[dx+i][dy-i] = 1
            if 0 <= dy+i < N:
                tmp[dx+i][dy+i] = 1

    return tmp

N = int(input())  # 판에 칸 개수

arr = [[0] * N for _ in range(N)]
cnt = 0
BackTracking(0, arr)

print(cnt)