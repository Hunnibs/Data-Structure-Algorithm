# 홀수만 더하기
def sol(cnt):
    sum = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            continue
        else:
            sum += arr[i]
    print('#' + str(cnt), sum)

T = int(input())
cnt = 1
for _ in range(T):
    arr = list(map(int, input().split()))
    sol(cnt)
    cnt += 1
