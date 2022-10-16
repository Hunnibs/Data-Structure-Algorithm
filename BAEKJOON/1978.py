N = int(input())
result = 0

A = list(map(int, input().split()))

for i in range(N):
    cnt = 0
    if A[i] == 1:
        continue
    else:
        for j in range(2, A[i]):
            if A[i] % j == 0:
                cnt += 1
                break
        
        if cnt != 1:
            result += 1

print(result)