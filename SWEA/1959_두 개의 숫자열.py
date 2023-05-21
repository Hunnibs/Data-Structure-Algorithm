T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    if len(A) < len(B):
        j = 0
        while j <= len(B)-len(A):
            tmp = 0
            for i in range(len(A)):
                tmp += (A[i] * B[i+j])
            j += 1
            result = max(result, tmp)
    else:
        j = 0
        while j <= len(A)-len(B):
            tmp = 0
            for i in range(len(B)):
                tmp += (A[i+j] * B[i])
            j += 1
            result = max(result, tmp)

    print('#' + str(t), result)